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
    const nearRoot = findExeNear(workspaceRoot);
    if (nearRoot) {
      candidates.push(nearRoot);
    }
  }
  const editor = vscode.window.activeTextEditor;
  if (editor && editor.document.uri.scheme === "file") {
    const nearFile = findExeNear(path.dirname(editor.document.uri.fsPath));
    if (nearFile) {
      candidates.push(nearFile);
    }
  }
  return candidates.find((candidate) => isFile(candidate));
}

/**
 * @param {string} startDir
 * @returns {string | undefined}
 */
function findExeNear(startDir) {
  let dir = startDir;
  for (let i = 0; i < 8 && dir; i += 1) {
    const candidate = path.join(dir, "Python_Uploader.exe");
    if (isFile(candidate)) {
      return candidate;
    }
    const parent = path.dirname(dir);
    if (parent === dir) {
      break;
    }
    dir = parent;
  }
  return undefined;
}

function workspaceHasUploader() {
  const folders = vscode.workspace.workspaceFolders || [];
  if (
    folders.some((folder) => isFile(path.join(folder.uri.fsPath, "Python_Uploader.exe")))
  ) {
    return true;
  }
  const configured = vscode.workspace
    .getConfiguration("Python_Uploader")
    .get("exePath", "");
  if (configured && isFile(configured)) {
    return true;
  }
  const editor = vscode.window.activeTextEditor;
  if (editor && editor.document.uri.scheme === "file") {
    return Boolean(findExeNear(path.dirname(editor.document.uri.fsPath)));
  }
  return folders.some((folder) => Boolean(findExeNear(folder.uri.fsPath)));
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
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    vscode.window.showWarningMessage(
      "Откройте файл .py — Uploader запустится с этим файлом."
    );
    return;
  }

  // Сначала диск, потом Uploader: иначе на робота уйдёт прошлый сохранённый .py.
  if (editor.document.isUntitled) {
    const savedUntitled = await editor.document.save();
    if (!savedUntitled) {
      vscode.window.showErrorMessage(
        "Не удалось сохранить файл перед отправкой в Python Uploader."
      );
      return;
    }
  }
  await vscode.workspace.saveAll(false);
  if (editor.document.isDirty) {
    const saved = await editor.document.save();
    if (!saved) {
      vscode.window.showErrorMessage(
        "Не удалось сохранить файл перед отправкой в Python Uploader."
      );
      return;
    }
  }

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
  context.subscriptions.push(
    vscode.window.onDidChangeActiveTextEditor(() => updateAvailability())
  );
}

function deactivate() {
  if (statusBarItem) {
    statusBarItem.dispose();
    statusBarItem = undefined;
  }
}

module.exports = { activate, deactivate };
