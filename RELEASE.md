# Python Uploader For mBot2

[Русский](RELEASE.md) · [English](RELEASE.en.md)

Пререлиз. Загрузка Python-программ на **mBot2 / CyberPi** по USB.

---

## Файлы в этом релизе

| Файл | Назначение |
|------|------------|
| `Python_Uploader.exe` | Программа для Windows |
| `Python_Uploader.exe.sha256` | Контрольная сумма SHA256 |

Скачайте оба файла с этой страницы релиза.

### Проверка целостности (PowerShell)

```powershell
Get-FileHash .\Python_Uploader.exe -Algorithm SHA256
Get-Content .\Python_Uploader.exe.sha256
```

Хеши должны совпасть.

---

## Проверка перед загрузкой программы

- Windows 10/11  
- mBot2 / CyberPi, питание включено  
- USB-кабель с передачей данных  
- Драйвер CH340 (`1A86:7523`)  
- Закрыт mLink и другие программы на том же COM

---

## Быстрый старт

1. Запустите `Python_Uploader.exe`.
2. Выберите файл `.py` (Обзор, drag-and-drop или аргумент командной строки).
3. Выберите порт **CyberPi / mBot2**.
4. **Загрузить на робота** или `Ctrl+Enter`.

Повторный запуск подставляет в запущенную программу новый файл `.py`.

```text
Python_Uploader.exe "C:\path\to\program.py"
```

---

## Важно

- Не загружайте на плату `cyberpi.py`, `mbot2.py`, `mbuild.py`, `event.py`, `pocket.py` — программа их не пропускает.
- На плате файл пишется как `/flash/main.py`.
- Версия: **0.1.1**

Полная документация — в [README](README.md) репозитория.

---

### Windows SmartScreen

Exe **не подписан**. Windows может показать «Windows защитил ваш компьютер».

Если скачали **отсюда** и SHA256 совпал: **Подробнее** → **Выполнить в любом случае**.

Не берите exe с посторонних сайтов.
