# Python Uploader For mBot2

**Language / Язык:** [Русский](README.md) · [English](README.en.md)

Upload Python programs to **mBot2 / CyberPi** over USB.

The app finds the robot on a COM port (CH340 chip), switches the board into upload mode, and writes your `.py` file to the robot — the same path used by the Makeblock Python editor. After upload, the program stays on the board and runs without a computer.

Club website: [юный-инженер.рф](https://юный-инженер.рф/)

---

## Download (Windows)

1. Open this repository’s [Releases](../../releases).
2. Download:
   - `Python_Uploader.exe`
   - `Python_Uploader.exe.sha256` (checksum)
3. Verify the file (PowerShell):

```powershell
Get-FileHash .\Python_Uploader.exe -Algorithm SHA256
Get-Content .\Python_Uploader.exe.sha256
```

The hashes must match (the `.sha256` file lists the expected SHA256 and file name).

### Windows SmartScreen warning

The exe is **not Authenticode-signed**. Windows may show:

> Windows protected your PC

That is expected for a small utility without a paid code-signing certificate. If you downloaded the file from this Releases page and the SHA256 matches:

1. Click **More info**
2. Then **Run anyway**

Do not download the exe from third-party mirrors — always check the hash against the release.

---

## Requirements

| Requirement | Notes |
|-------------|--------|
| Windows 10/11 | The exe build targets Windows |
| mBot2 / CyberPi | Power switch on |
| USB data cable | Charge-only cables will not work |
| CH340 driver | VID:PID `1A86:7523` |
| mLink closed | And any other app holding the same COM port |

---

## How to use

1. Connect the robot over USB and turn power on.
2. Run `Python_Uploader.exe`.
3. Choose a program file (`.py`) — **Browse**, drag-and-drop into the window, or pass the path as an argument.
4. In the port list, select **CyberPi / mBot2**.
5. Click **Upload to robot** (or press `Ctrl+Enter`).

Starting the exe again with a new `.py` **does not open a second window**: the path is handed to the running instance and the window is brought to the front.

### Launch with a file from the command line

```text
Python_Uploader.exe "C:\path\to\program.py"
```

### UI features

- USB port list labeled CyberPi / mBot2
- Upload log (save, clear, timestamps)
- Themes: system / light / dark
- Language: русский / English
- Cancel during upload

Settings are stored in `%LOCALAPPDATA%\Python_Uploader\`.

---

## VS Code

The project includes an extension that binds a status-bar button to the exe and the current `${file}`, and supports launch with the F5 hotkey.
The task starts `Python_Uploader.exe` with the path to the open `.py`. If a window is already open, the new file is substituted.

---

## Notes

- Do not upload stub files `cyberpi.py`, `mbot2.py`, `mbuild.py`, `event.py`, `pocket.py` — the app skips them.
- On the board the file is written as `/flash/main.py` (same as Makeblock’s editor).
- Version: **0.1.0**

---

## Feedback

Questions and suggestions — via Issues in this repository or the club site [юный-инженер.рф](https://юный-инженер.рф/).
