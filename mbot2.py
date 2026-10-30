"""Сигнатуры библиотеки mBot2 для VS Code.

На CyberPi модуль ``mbot2`` уже вшит в прошивку. Этот файл нужен редактору:
автодополнение, подсказки и проверка вызовов. На компьютере функции ничего
не делают и робота не двигают.

В mBlock заливайте только свою программу (``import mbot2``). Этот файл
на плату копировать не нужно: он подменит настоящую библиотеку.
"""

from __future__ import annotations

from typing import Literal

Duration = float | Literal["null"]
Port = int | Literal[
    "all",
    "EM1",
    "EM2",
    "M1",
    "M2",
    "S1",
    "S2",
    "S3",
    "S4",
]
ColorName = Literal[
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "purple",
    "white",
    "black",
]

__all__ = [
    "forward",
    "backward",
    "turn_left",
    "turn_right",
    "straight",
    "turn",
    "stop",
    "drive_power",
    "drive_speed",
    "EM_stop",
    "EM_set_power",
    "EM_set_speed",
    "EM_turn",
    "EM_get_angle",
    "EM_get_speed",
    "EM_get_power",
    "EM_reset_angle",
    "EM_lock",
    "motor_add",
    "motor_set",
    "motor_get",
    "motor_drive",
    "motor_stop",
    "servo_add",
    "servo_set",
    "servo_get",
    "servo_release",
    "servo_drive",
    "led_on",
    "led_show",
    "led_move",
    "led_off",
    "led_add_bri",
    "led_set_bri",
    "led_get_bri",
    "write_digital",
    "read_digital",
    "set_pwm",
    "read_analog",
]


def forward(speed: float = 50, t: Duration = "null") -> None:
    """Ехать вперёд.

    speed: обороты моторов, от -200 до 200. Отрицательное значение — назад.
    t: секунды. ``"null"`` — ехать, пока не придёт команда остановки.
    """


def backward(speed: float = 50, t: Duration = "null") -> None:
    """Ехать назад.

    speed: обороты моторов, от -200 до 200. Отрицательное значение — вперёд.
    t: секунды. ``"null"`` — ехать, пока не придёт команда остановки.
    """


def turn_left(speed: float = 50, t: Duration = "null") -> None:
    """Повернуть налево.

    speed: обороты моторов, от -200 до 200. Отрицательное значение — направо.
    t: секунды. ``"null"`` — крутиться, пока не придёт команда остановки.
    """


def turn_right(speed: float = 50, t: Duration = "null") -> None:
    """Повернуть направо.

    speed: обороты моторов, от -200 до 200. Отрицательное значение — налево.
    t: секунды. ``"null"`` — крутиться, пока не придёт команда остановки.
    """


def straight(distance: float, speed: float = 50) -> None:
    """Проехать заданную дистанцию.

    distance: сантиметры. Отрицательное значение — назад.
    speed: обороты, от 0 до 200. По умолчанию 50.
    Вызов блокирует программу, пока дистанция не пройдена или не вызван stop().
    """


def turn(angle: int, speed: float = 50) -> None:
    """Повернуть на заданный угол по часовой стрелке.

    angle: градусы. Отрицательное значение — против часовой.
    speed: обороты, от 0 до 200. По умолчанию 50.
    Вызов блокирует программу, пока угол не пройден или не вызван stop().
    """


def stop() -> None:
    """Остановить движение шасси."""


def drive_power(EM1_power: float, EM2_power: float) -> None:
    """Задать мощность левого (EM1) и правого (EM2) моторов.

    Мощность каждого мотора: от -100 до 100, в процентах.
    Плюс — вал крутится против часовой стрелки.
    """


def drive_speed(EM1_speed: float, EM2_speed: float) -> None:
    """Задать скорость левого (EM1) и правого (EM2) моторов.

    Скорость каждого мотора: от -200 до 200 оборотов в минуту.
    Плюс — вал крутится против часовой стрелки.
    """


def EM_stop(port: Port = "all") -> None:
    """Остановить энкодерный мотор.

    port: ``"all"``, ``"EM1"``, ``"EM2"``, ``1`` или ``2``.
    """


def EM_set_power(power: float, port: Port = "all") -> None:
    """Задать мощность энкодерного мотора, от -100 до 100 процентов.

    port: ``"all"``, ``"EM1"``, ``"EM2"``, ``1`` или ``2``.
    """


def EM_set_speed(speed: float, port: Port = "all") -> None:
    """Задать скорость энкодерного мотора, от -200 до 200 оборотов в минуту.

    port: ``"all"``, ``"EM1"``, ``"EM2"``, ``1`` или ``2``.
    """


def EM_turn(angle: int, speed: float, port: Port = "all") -> None:
    """Повернуть энкодерный мотор на угол против часовой стрелки.

    speed: от 0 до 200 оборотов в минуту.
    Вызов блокирует программу до конца поворота или до stop().
    """


def EM_get_angle(port: Port) -> int:
    """Угол энкодерного мотора в градусах. Растёт против часовой стрелки."""
    return 0


def EM_get_speed(port: Port) -> int:
    """Текущая скорость энкодерного мотора, обороты в минуту."""
    return 0


def EM_get_power(port: Port) -> int:
    """Текущая мощность энкодерного мотора, от -100 до 100 процентов."""
    return 0


def EM_reset_angle(port: Port = "all") -> None:
    """Сбросить накопленный угол энкодерного мотора."""


def EM_lock(is_lock: bool = False, port: Port = "all") -> None:
    """Удержание позиции энкодерного мотора. По умолчанию выключено."""


def motor_add(power: float, port: Port) -> None:
    """Изменить мощность мотора постоянного тока на port M1/M2.

    power: прибавка в процентах, от -200 до 200.
    port: ``"all"``, ``"M1"``, ``"M2"``, ``1`` или ``2``.
    """


def motor_set(power: float, port: Port) -> None:
    """Задать мощность мотора постоянного тока, от -100 до 100 процентов.

    port: ``"all"``, ``"M1"``, ``"M2"``, ``1`` или ``2``.
    """


def motor_get(port: Port) -> float:
    """Текущая мощность мотора постоянного тока, от -100 до 100 процентов."""
    return 0.0


def motor_drive(power1: float, power2: float) -> None:
    """Задать мощность моторов на портах M1 и M2, каждый от -100 до 100."""


def motor_stop(port: Port) -> None:
    """Остановить мотор постоянного тока.

    port: ``"all"``, ``"M1"``, ``"M2"``, ``1`` или ``2``.
    """


def servo_add(angle: int, port: Port) -> None:
    """Сдвинуть сервопривод на angle градусов, от -180 до 180.

    port: ``"all"``, ``"S1"``…``"S4"``, ``1``…``4``.
    """


def servo_set(angle: int, port: Port) -> None:
    """Поставить сервопривод в угол от 0 до 180 градусов.

    port: ``"all"``, ``"S1"``…``"S4"``, ``1``…``4``.
    """


def servo_get(port: Port) -> int:
    """Последний заданный угол сервопривода, от 0 до 180
    
    port: ``"all"``, ``"S1"``…``"S4"``, ``1``…``4``."""
    return 0


def servo_release(port: Port) -> None:
    """Отпустить сервопривод: вал больше не удерживается.

    port: ``"all"``, ``"S1"``…``"S4"``, ``1``…``4``.
    """


def servo_drive(angle1: int, angle2: int, angle3: int, angle4: int) -> None:
    """Задать углы сервоприводов S1, S2, S3 и S4. Каждый угол от 0 до 180."""


def led_on(
    r: int | ColorName,
    g: int = 0,
    b: int = 0,
    id: int | Literal["all"] = "all",
    port: Port = "all",
) -> None:
    """Зажечь светодиод ленты.

    r, g, b: 0–255. В r можно передать имя цвета: ``"red"``, ``"green"`` и т.д.
    id: номер светодиода 1–36 или ``"all"``.
    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_show(color: str, port: Port) -> None:
    """Задать цвета всей ленты строкой: ``"r g b y"``.

    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_move(step: int, cycle: int, port: Port) -> None:
    """Сдвинуть цвета ленты на step позиций. cycle — длина цикла, 1–36.

    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_off(id: int | Literal["all"] = "all", port: Port = "all") -> None:
    """Погасить светодиод или всю ленту.

    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_add_bri(brightness: int, port: Port) -> None:
    """Изменить яркость ленты на brightness процентов, от -100 до 100."""


def led_set_bri(brightness: int, port: Port) -> None:
    """Задать яркость ленты в процентах, от -100 до 100."""


def led_get_bri(port: Port) -> int:
    """Текущая яркость ленты в процентах."""
    return 0


def write_digital(val: int | bool, port: Port) -> None:
    """Записать цифровой уровень на пин.

    val: ``True``/``1`` — высокий, ``False``/``0`` — низкий.
    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def read_digital(port: Port) -> int:
    """Прочитать цифровой уровень пина: 0 или 1."""
    return 0


def set_pwm(duty: int, frequency: int, port: Port) -> None:
    """Выдать ШИМ.

    duty: скважность 0–100 процентов.
    frequency: частота 1–2000 Гц.
    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def read_analog(port: Port) -> float:
    """Прочитать напряжение на пине, от 0 до 5 вольт."""
    return 0.0
