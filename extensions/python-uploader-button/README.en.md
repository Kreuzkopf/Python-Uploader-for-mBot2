# Python Uploader Button extension for VS Code

**Language / Язык:** [Русский](README.md) · [English](README.en.md)

A blue **→ Uploader** button in the Cursor/VS Code status bar and the **F5** key.

Starts `Python_Uploader.exe` and passes the path to the open `.py` file.
F5 does this only in a folder that contains `Python_Uploader.exe`. In other projects F5 still starts the debugger as usual.

The button is not enabled automatically from the project folder. Install the extension into the editor once.

## Install

From the root of this folder:

```powershell
.\.vscode\extensions\python-uploader-button\install.ps1
```

Or in Cursor: `Ctrl+Shift+P` → **Extensions: Install from Location...** → select the `.vscode\extensions\python-uploader-button` folder.

After install: Reload Window if the button does not appear yet.

`pack_vsix.py` builds the extension package. `install.ps1` runs it and installs the package into Cursor or VS Code. These two files are needed when setting up the computer, not when uploading a program to the robot.

## Path to the exe

By default the extension uses `Python_Uploader.exe` in the root of the open folder.
If the file is elsewhere: Settings → `Python_Uploader.exePath`.
