# Расширение Python Uploader Button для VS Code

[Русский](README.md) · [English](README.en.md)

Синяя кнопка **→ Uploader** в статус-баре VS Code и клавиша **F5**.

Нажатие F5 запускает Uploader `Python_Uploader.exe` и передаёт путь к открытому `.py`.
Перед запуском выполняется сохранение файла.

Для работы кнопки необходимо однократно установить расширение в редакторе.

## Установка

Из корня этой папки:

```powershell
.\extensions\python-uploader-button\install.ps1
```

Или в Cursor: `Ctrl+Shift+P` → **Extensions: Install from VSIX...** → `extensions\python-uploader-button\python-uploader-button.vsix`.

После установки: Reload Window, если кнопки ещё нет.

`pack_vsix.py` собирает пакет расширения. `install.ps1` вызывает его и ставит пакет в Cursor или VS Code. Эти два файла нужны при установке на компьютер.

## Путь к exe

По умолчанию берётся `Python_Uploader.exe` в корне открытой папки.
Если файл лежит в другом месте: Settings → `Python_Uploader.exePath`.
