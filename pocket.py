"""Сигнатуры Pocket Shield для VS Code.

На CyberPi доступны как ``cyberpi.pocket``. Этот файл нужен редактору:
автодополнение, подсказки и проверка вызовов. На компьютере функции ничего
не делают.

В mBlock заливайте только свою программу. Этот файл на плату копировать
не нужно: он подменит настоящую библиотеку.

Список — из Python API Documentation for CyberPi, раздел APIs for Extension
Boards → Pocket Shield. Shield: 2 порта моторов (M1/M2), 2 цифровых порта
серво/лент/датчиков (S1/S2) и батарея (уровень — ``cyberpi.get_battery()``).
"""

from __future__ import annotations

from typing import Literal

Port = int | Literal[
    "all",
    "M1",
    "M2",
    "S1",
    "S2",
]
MotorPort = int | Literal["all", "M1", "M2"]
ServoPort = int | Literal["all", "S1", "S2"]
PinPort = int | Literal["all", "S1", "S2"]
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


def motor_add(power: float, port: MotorPort) -> None:
    """Изменить мощность мотора постоянного тока.

    power: прибавка в процентах, от -200 до 200.
    port: ``"all"``, ``"M1"``, ``"M2"``, ``1`` или ``2``.
    """


def motor_set(power: float, port: MotorPort) -> None:
    """Задать мощность мотора, от -100 до 100 процентов.

    Плюс — вал против часовой стрелки (зависит от мотора).
    port: ``"all"``, ``"M1"``, ``"M2"``, ``1`` или ``2``.
    """


def motor_get(port: MotorPort) -> float:
    """Текущая мощность мотора, от -100 до 100 процентов.

    port: ``"M1"``, ``"M2"``, ``1`` или ``2``.
    """
    return 0.0


def motor_drive(power1: float, power2: float) -> None:
    """Задать мощность моторов M1 и M2, каждый от -100 до 100 процентов."""


def motor_stop(port: MotorPort) -> None:
    """Остановить мотор (мощность 0).

    port: ``"all"``, ``"M1"``, ``"M2"``, ``1`` или ``2``.
    """


def servo_add(angle: int, port: ServoPort) -> None:
    """Сдвинуть сервопривод на angle градусов, от -180 до 180.

    Если раньше не вызывали ``servo_set``, серво сначала встаёт на 20°,
    затем сдвигается на angle.
    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def servo_set(angle: int, port: ServoPort) -> None:
    """Поставить сервопривод в угол от 0 до 180 градусов.

    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def servo_get(port: ServoPort) -> int:
    """Последний заданный угол сервопривода, от 0 до 180.

    После ``servo_release`` или ручного поворота значение может быть неточным.
    port: ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """
    return 0


def servo_release(port: ServoPort) -> None:
    """Отпустить сервопривод: вал больше не удерживается.

    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def servo_drive(angle1: int, angle2: int) -> None:
    """Задать углы сервоприводов S1 и S2. Каждый угол от 0 до 180."""


def led_on(
    r: int | ColorName,
    g: int = 0,
    b: int = 0,
    id: int | Literal["all"] = "all",
    port: ServoPort = "all",
) -> None:
    """Зажечь светодиод ленты на порту S1/S2.

    r, g, b: 0–255. В r можно передать имя цвета: ``"red"``, ``"green"`` и т.д.
    id: номер светодиода 1–36 или ``"all"``.
    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_show(color: str, port: ServoPort) -> None:
    """Задать цвета всей ленты строкой: ``"r g b y"``.

    До 36 цветов; лишние отбрасываются.
    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_move(step: int, cycle: int, port: ServoPort) -> None:
    """Сдвинуть цвета ленты на step позиций. cycle — длина цикла, 1–36.

    step: от -36 до 36.
    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_off(id: int | Literal["all"] = "all", port: ServoPort = "all") -> None:
    """Погасить светодиод или всю ленту.

    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_add_bri(brightness: int, port: ServoPort) -> None:
    """Изменить яркость ленты на brightness процентов, от -100 до 100.

    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_set_bri(brightness: int, port: ServoPort) -> None:
    """Задать яркость ленты, 0–100 процентов.

    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def led_get_bri(port: ServoPort) -> int:
    """Текущая яркость ленты в процентах.

    port: ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """
    return 0


def write_digital(val: int | bool, port: PinPort) -> None:
    """Записать цифровой уровень на пин S1/S2 (Arduino-модули).

    val: ``True``/``1`` — высокий, ``False``/``0`` — низкий.
    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def read_digital(port: PinPort) -> int:
    """Прочитать цифровой уровень пина: 0 или 1.

    port: ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """
    return 0


def set_pwm(duty: int, frequency: int, port: PinPort) -> None:
    """Выдать ШИМ на пин.

    duty: скважность 0–100 процентов.
    frequency: частота 1–2000 Гц.
    port: ``"all"``, ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """


def read_analog(port: PinPort) -> float:
    """Прочитать напряжение на пине, от 0 до 5 вольт.

    port: ``"S1"``, ``"S2"``, ``1`` или ``2``.
    """
    return 0.0
