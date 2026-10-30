# Python Uploader For mBot2

**Язык / Language:** [Русский](README.md) · [English](README.en.md)

Upload Python programs to **mBot2 / CyberPi** over USB.

<img width="758" height="692" alt="image" src="https://github.com/user-attachments/assets/79a3d8c4-91b7-40a1-a0e8-381497303c10" />

The program finds the robot on a COM port, puts the board into upload mode, and sends the `.py` file to the robot — the same place the Makeblock editor writes it. After upload, the program stays on the board and runs without a computer.

---

## Download (Windows)

1. Open the [Releases](../../releases) page of this repository.
2. Download:
   - `Python_Uploader.exe`
   - `Python_Uploader.exe.sha256` (checksum)
3. Check the file (PowerShell):

```powershell
Get-FileHash .\Python_Uploader.exe -Algorithm SHA256
Get-Content .\Python_Uploader.exe.sha256
```

The hashes must match (the `.sha256` file contains the expected SHA256 and the file name).

---

## How to use

1. Connect the robot over USB and turn the power on.
2. Start `Python_Uploader.exe`.
3. Choose the `.py` program — with **Browse**, by dropping the file onto the window, or by passing the path as an argument.
4. In the port list, select **CyberPi / mBot2**.
5. Click **Upload to the robot** (or press `Ctrl+Enter`).

### Start with a file from the command line

```text
Python_Uploader.exe "C:\path\to\program.py"
```

### Interface

- USB port list, with CyberPi / mBot2 marked
- Upload log (save, clear, timestamps)
- Themes: match the system / light / dark
- Language: Russian / English
- Cancel while an upload is in progress

Settings are stored in `%LOCALAPPDATA%\Python_Uploader\`.

---

## Check before upload

| Requirement | Notes |
|-------------|--------|
| Windows 10/11 | The build targets Windows |
| mBot2 / CyberPi | Power is on |
| USB cable that carries data | Charge-only cables will not work |
| CH340 driver | VID:PID `1A86:7523` |
| mLink is closed | And any other program using the same COM port |

---

## VS Code

`mbot2.py`, `mbuild.py`, `cyberpi.py`, `pocket.py`, and `event.py` are method signatures. They match the official mBot2 / CyberPi API in full and make the program easier to write in VS Code: the editor shows hints, autocomplete, and checks calls. On the computer these functions do nothing and do not affect the robot. The board already has the real firmware modules, so the signature files themselves must not be uploaded.

<img width="808" height="364" alt="advice" src="https://github.com/user-attachments/assets/471640b7-d5ae-49a3-bbe2-68767372a4f7" />

The project includes an extension that binds a status-bar button to launching the program, and also launch with the F5 hotkey.
Tasks starts `Python_Uploader.exe` with the path to the open `.py`. If the window is already open, the new file is filled in.

<img width="436" height="226" alt="uploader" src="https://github.com/user-attachments/assets/1e90509f-faa8-4842-a70e-4b90b40d520f" />

---

## Important

- Do not upload `cyberpi.py`, `mbot2.py`, `mbuild.py`, `event.py`, or `pocket.py` to the board — the program does not accept them.
- The controller receives `/flash/main.py`, the same way as in the Makeblock editor.

---

## Windows SmartScreen warning

The exe is **not** signed with an Authenticode certificate, so Windows may show a warning:

> Windows protected your PC

This is expected for a small utility without a paid code-signing certificate. If you downloaded the file from this Releases page and the SHA256 matches:

1. Click **More info**
2. Then **Run anyway**

Do not download the program from unofficial mirrors — check the hash against the release.

---

## Feedback

Questions and suggestions: Issues in this repository, or the club site [юный-инженер.рф](https://юный-инженер.рф/).
