# Расширение Python Uploader Button для VS Code

**Язык / Language:** [Русский](README.md) · [English](README.en.md)

Синяя кнопка **→ Uploader** в статус-баре Cursor/VS Code и клавиша **F5**.

Запускает `Python_Uploader.exe` и передаёт путь к открытому `.py`.
Перед запуском сохраняет файлы. F5 на `.py` запускает Uploader, а не меню отладчика.

Кнопка сама из папки проекта не включается. Её нужно один раз установить в редактор.

## Установка

Из корня этой папки:

```powershell
.\extensions\python-uploader-button\install.ps1
```

Или в Cursor: `Ctrl+Shift+P` → **Extensions: Install from VSIX...** → `extensions\python-uploader-button\python-uploader-button.vsix`.

После установки: Reload Window, если кнопки ещё нет.

`pack_vsix.py` собирает пакет расширения. `install.ps1` вызывает его и ставит пакет в Cursor или VS Code. Эти два файла нужны при установке на компьютер, не при загрузке программы на робота.

## Путь к exe

По умолчанию берётся `Python_Uploader.exe` в корне открытой папки.
Если файл лежит в другом месте: Settings → `Python_Uploader.exePath`.
