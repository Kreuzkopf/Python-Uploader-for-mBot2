# Python Uploader For mBot2

[Русский]

Пререлиз **0.1.6**. Загрузка Python-программ и проектов mBlock на **mBot2 / CyberPi** по USB и Bluetooth.

---

## Что нового в 0.1.6

- Кнопка **Обновить** в том же стиле, что **Обзор** (без акцентной скруглённой рамки).
- Если прошивка старше 44.01.016, а робот подключён по Bluetooth, кнопка остаётся на месте, но серая. Нажатие пишет в журнал, что прошивка возможна только по USB-кабелю.
- Обновлена иконка выбора файла mBlock.

---

## Что нового в 0.1.5

- Кнопка **Обновить** под картинкой робота: USB-образ CyberPi **44.01.016** из официального плагина mBlock 1.1.46 (esptool, как mLink). Кнопка видна только если на плате прошивка старше 016.
- Платы с 016 и новее не прошиваются. Bluetooth для прошивки не используется.
- Можно выбрать не только `.py`, но и проект **mBlock** (`.mblock`): иконка Python открывает обзор `.py`, иконка с пандой mBlock — `.mblock`, **Обзор** — все подходящие расширения.

---

## Что нового в 0.1.4

- Список роботов больше не прыгает: **USB всегда сверху**, Bluetooth сохраняет порядок, в котором роботы были найдены.
- У Bluetooth показывается **уровень сигнала** (полоски и RSSI). Сигнал обновляется в той же строке, без перестановки списка.
- Короткие подписи портов, например:
  - `USB  COM6  44.01.011`
  - `BLE  Makeblock_LE C3F1  ▂▄▆█ -52`
- Подключённый робот помечен `●`. Чужой COM отображается коротко: `COM5  ·  другой`.

---

## Файлы в этом релизе

| Файл | Назначение |
|------|------------|
| `Python_Uploader.exe` | Программа для Windows |
| `Python_Uploader.exe.sha256` | Контрольная сумма SHA256 |
| `cyberpi.py`, `event.py`, `mbot2.py`, `mbuild.py`, `pocket.py` | Сигнатуры API для VS Code (на робота не загружать) |

Скачайте программу и файл контрольной суммы с этой страницы релиза.

### Проверка целостности (PowerShell)

```powershell
Get-FileHash .\Python_Uploader.exe -Algorithm SHA256
Get-Content .\Python_Uploader.exe.sha256
```

Хеши должны совпасть.

Ожидаемый SHA256:

```
e78c3889c1698ad1f46fbc0fc45211c5141a33ee254b061d1c566c19f24c55fa
```

---

## Проверка перед загрузкой программы

- Windows 10/11  
- mBot2 / CyberPi, питание включено  
- USB-кабель с передачей данных или включённый Bluetooth на компьютере  
- Для USB: установлен драйвер CH340 (`1A86:7523`)  
- Закрыт mLink и другие программы, подключённые к роботу

---

## Быстрый старт

1. Запустите `Python_Uploader.exe`.
2. Выберите робота в списке (USB сверху, Bluetooth с уровнем сигнала) и нажмите **Соединиться**.
3. Выберите файл `.py` (Обзор, drag-and-drop или аргумент командной строки).
4. **Загрузить на робота** или `Ctrl+Enter`.

Повторный запуск подставляет в запущенную программу новый файл `.py`.

```text
Python_Uploader.exe "C:\path\to\program.py"
```

---

## Важно

- Не загружайте на плату `cyberpi.py`, `mbot2.py`, `mbuild.py`, `event.py`, `pocket.py` — программа их не пропускает.
- На плате файл пишется как `/flash/main.py`.
- Версия: **0.1.6** (пререлиз)

Полная документация — в [README](https://github.com/Kreuzkopf/Python-Uploader-for-mBot2/blob/main/README.md) репозитория.

---

### Windows SmartScreen

Exe **не подписан**. Windows может показать «Windows защитил ваш компьютер».

Если скачали **отсюда** и SHA256 совпал: **Подробнее** → **Выполнить в любом случае**.

Не берите exe с посторонних сайтов.

---

[English]

Pre-release **0.1.6**. Upload Python programs and mBlock projects to **mBot2 / CyberPi** over USB and Bluetooth.

---

## What's new in 0.1.6

- The **Update** button uses the same style as **Browse** (no accent rounded look).
- If firmware is older than 44.01.016 and the robot is on Bluetooth, the button stays visible but greyed out. Clicking it writes to the log that firmware update needs a USB cable.
- Updated mBlock file-picker icon.

---

## What's new in 0.1.5

- **Update** button under the robot picture: official CyberPi USB image **44.01.016** from mBlock plugin 1.1.46 (esptool, same as mLink). The button appears only when the board firmware is older than 016.
- Boards already on 016 or newer are not flashed. Bluetooth cannot be used for firmware update.
- You can choose not only `.py` but also an **mBlock** project (`.mblock`): the Python icon browses `.py`, the mBlock panda icon browses `.mblock`, **Browse** shows all supported extensions.

---

## What's new in 0.1.4

- The robot list no longer jumps: **USB stays at the top**, Bluetooth keeps the order in which robots were found.
- Bluetooth rows show **signal strength** (bars and RSSI). The signal updates in place without reshuffling the list.
- Shorter port labels, for example:
  - `USB  COM6  44.01.011`
  - `BLE  Makeblock_LE C3F1  ▂▄▆█ -52`
- The connected robot is marked with `●`. A non-robot COM port is shown as `COM5  ·  other`.

---

## Assets in this release

| File | Purpose |
|------|---------|
| `Python_Uploader.exe` | Windows application |
| `Python_Uploader.exe.sha256` | SHA256 checksum |
| `cyberpi.py`, `event.py`, `mbot2.py`, `mbuild.py`, `pocket.py` | VS Code API stubs (do not upload these to the robot) |

Download the application and the checksum file from this release page.

### Verify integrity (PowerShell)

```powershell
Get-FileHash .\Python_Uploader.exe -Algorithm SHA256
Get-Content .\Python_Uploader.exe.sha256
```

The hashes must match.

Expected SHA256:

```
e78c3889c1698ad1f46fbc0fc45211c5141a33ee254b061d1c566c19f24c55fa
```

---

## Checklist before uploading

- Windows 10/11  
- mBot2 / CyberPi, power on  
- USB data cable or Bluetooth enabled on the PC  
- For USB: CH340 driver (`1A86:7523`) installed  
- mLink and other apps connected to the robot closed

---

## Quick start

1. Run `Python_Uploader.exe`.
2. Select a robot in the list (USB at the top, Bluetooth with signal strength) and click **Connect**.
3. Choose a `.py` file (Browse, drag-and-drop, or command-line argument).
4. **Upload to robot** or press `Ctrl+Enter`.

Running it again passes the new `.py` file to the already running application.

```text
Python_Uploader.exe "C:\path\to\program.py"
```

---

## Important

- Do not upload `cyberpi.py`, `mbot2.py`, `mbuild.py`, `event.py`, `pocket.py` to the board — the app blocks them.
- On the board, the file is saved as `/flash/main.py`.
- Version: **0.1.6** (pre-release)

Full documentation is in the repository [README](https://github.com/Kreuzkopf/Python-Uploader-for-mBot2/blob/main/README.en.md).

---

### Windows SmartScreen

The exe is **not signed**. Windows may show “Windows protected your PC”.

If you downloaded it **from here** and the SHA256 matches: **More info** → **Run anyway**.

Do not download the exe from third-party sites.
