const vscode = require("vscode");
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");

/** @type {vscode.StatusBarItem | undefined} */
let statusBarItem;

/**
 * @param {string} filePath
 * @returns {boolean}
 */
function isFile(filePath) {
  try {
    return Boolean(filePath) && fs.existsSync(filePath) && fs.statSync(filePath).isFile();
  } catch {
    return false;
  }
}

/**
 * @param {string} workspaceRoot
 * @param {string} configured
 * @returns {string | undefined}
 */
function resolveExePath(workspaceRoot, configured) {
  const candidates = [];
  if (configured && configured.trim()) {
    const raw = configured.trim();
    if (path.isAbsolute(raw)) {
      candidates.push(raw);
    } else if (workspaceRoot) {
      candidates.push(path.join(workspaceRoot, raw));
    } else {
      candidates.push(raw);
    }
  }
  if (workspaceRoot) {
    candidates.push(path.join(workspaceRoot, "Python_Uploader.exe"));
  }
  return candidates.find((candidate) => isFile(candidate));
}

/**
 * @returns {boolean}
 */
function workspaceHasUploader() {
  const folders = vscode.workspace.workspaceFolders || [];
  return folders.some((folder) =>
    isFile(path.join(folder.uri.fsPath, "Python_Uploader.exe"))
  );
}

function updateAvailability() {
  return vscode.commands.executeCommand(
    "setContext",
    "pythonUploader.available",
    workspaceHasUploader()
  );
}

/**
 * @returns {string | undefined}
 */
function currentPyFile() {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    return undefined;
  }
  const file = editor.document.uri;
  if (file.scheme !== "file") {
    return undefined;
  }
  if (!file.fsPath.toLowerCase().endsWith(".py")) {
    return undefined;
  }
  return file.fsPath;
}

/**
 * @param {string} pyFile
 * @returns {string}
 */
function workspaceRootFor(pyFile) {
  const folders = vscode.workspace.workspaceFolders || [];
  const match = folders.find((folder) => {
    const root = folder.uri.fsPath;
    const file = pyFile.toLowerCase();
    const prefix = root.toLowerCase();
    return file === prefix || file.startsWith(prefix + path.sep);
  });
  if (match) {
    return match.uri.fsPath;
  }
  return folders[0] ? folders[0].uri.fsPath : "";
}

async function launchUploader() {
  const pyFile = currentPyFile();
  if (!pyFile) {
    vscode.window.showWarningMessage(
      "Откройте файл .py — Uploader запустится с этим файлом."
    );
    return;
  }

  const root = workspaceRootFor(pyFile);
  const configured = vscode.workspace
    .getConfiguration("Python_Uploader")
    .get("exePath", "");
  const exePath = resolveExePath(root, configured);

  if (!exePath) {
    vscode.window.showErrorMessage(
      "Не найден Python_Uploader.exe в папке проекта. Укажите путь в настройке Python_Uploader.exePath."
    );
    return;
  }

  spawn(exePath, [pyFile], {
    detached: true,
    stdio: "ignore",
    windowsHide: true,
  }).unref();
}

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
  updateAvailability();

  statusBarItem = vscode.window.createStatusBarItem(
    vscode.StatusBarAlignment.Left,
    1000
  );
  statusBarItem.text = "$(arrow-right) Uploader";
  statusBarItem.tooltip = "Python Uploader: открыть текущий .py (F5)";
  statusBarItem.command = "PythonUploader.launch";
  statusBarItem.color = "#7ec8ff";
  statusBarItem.backgroundColor = new vscode.ThemeColor(
    "statusBarItem.prominentBackground"
  );
  statusBarItem.show();

  context.subscriptions.push(statusBarItem);
  context.subscriptions.push(
    vscode.commands.registerCommand("PythonUploader.launch", launchUploader)
  );
  context.subscriptions.push(
    vscode.workspace.onDidChangeWorkspaceFolders(updateAvailability)
  );
}

function deactivate() {
  if (statusBarItem) {
    statusBarItem.dispose();
    statusBarItem = undefined;
  }
}

module.exports = { activate, deactivate };
