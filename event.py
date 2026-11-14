"""Сигнатуры модуля ``event`` для VS Code.

На CyberPi модуль уже вшит в прошивку. Этот файл нужен редактору.
На компьютере функции ничего не делают.

В mBlock заливайте только свою программу. Этот файл на плату копировать
не нужно.

Список функций — со страницы Python API Documentation for CyberPi, раздел Events.
Там имена записаны как ``cyberpi.event``. Залитая программа mBlock
подключает тот же модуль через ``import event``.

События ``event`` работают только в режиме Upload.

Заголовок срабатывает в момент события. Кнопка, которую держат
нажатой, обработчик повторно не запускает.

Страница ``event`` для Halocode (``shaked``, ``touchpad``, ``mesh_message``)
описывает другую плату. ``mesh_broadcast`` для CyberPi — из Function Extension.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Literal, TypeVar

F = TypeVar("F", bound=Callable[..., object])


def _keep(callback: F) -> F:
    return callback


def start(callback: F) -> F:
    """Запуск программы на CyberPi: ``@event.start``."""
    return callback


def is_press(
    name: Literal[
        "a",
        "b",
        "up",
        "down",
        "left",
        "right",
        "middle",
        "any_direction",
        "any_button",
        "any",
    ],
) -> Callable[[F], F]:
    """Кнопку нажали или джойстик сдвинули: ``@event.is_press("a")``.

    name: ``a``, ``b``, ``up``, ``down``, ``left``, ``right``, ``middle``,
    ``any_direction``, ``any_button``, ``any``.
    """
    return _keep


def is_tiltforward(callback: F) -> F:
    """Плату наклонили вперёд."""
    return callback


def is_tiltback(callback: F) -> F:
    """Плату наклонили назад."""
    return callback


def is_tiltleft(callback: F) -> F:
    """Плату наклонили влево."""
    return callback


def is_tiltright(callback: F) -> F:
    """Плату наклонили вправо."""
    return callback


def is_faceup(callback: F) -> F:
    """Экран оказался сверху."""
    return callback


def is_facedown(callback: F) -> F:
    """Экран оказался снизу."""
    return callback


def is_stand(callback: F) -> F:
    """Плата встала вертикально, светодиоды снизу.

    В истории изменений официальной страницы событие добавлено
    2020-09-29. В текущем списке заголовков его нет.
    """
    return callback


def is_handstand(callback: F) -> F:
    """Плата встала вертикально, светодиоды сверху.

    В истории изменений официальной страницы событие добавлено
    2020-09-29. В текущем списке заголовков его нет.
    """
    return callback


def is_shake(callback: F) -> F:
    """Плату встряхнули."""
    return callback


def is_waveup(callback: F) -> F:
    """Плату взмахнули вверх."""
    return callback


def is_wavedown(callback: F) -> F:
    """Плату взмахнули вниз."""
    return callback


def is_waveleft(callback: F) -> F:
    """Плату взмахнули влево."""
    return callback


def is_waveright(callback: F) -> F:
    """Плату взмахнули вправо."""
    return callback


def is_freefall(callback: F) -> F:
    """Плата падает."""
    return callback


def is_clockwise(callback: F) -> F:
    """Плату поворачивают по часовой стрелке вокруг оси z."""
    return callback


def is_anticlockwise(callback: F) -> F:
    """Плату поворачивают против часовой стрелки вокруг оси z."""
    return callback


def greater_than(
    threshold: int,
    type: Literal["microphone", "light_sensor", "shake_val", "timer"],
) -> Callable[[F], F]:
    """Значение стало больше порога: ``@event.greater_than(50, "microphone")``.

    threshold: порог от 0 до 100.
    
    type: ``microphone``, ``light_sensor``, ``shake_val``, ``timer``.
    """
    return _keep


def smaller_than(
    threshold: int,
    type: Literal["microphone", "light_sensor", "shake_val", "timer"],
) -> Callable[[F], F]:
    """Значение стало меньше порога: ``@event.smaller_than(50, "light_sensor")``.

    threshold: порог от 0 до 100.
    
    type: ``microphone``, ``light_sensor``, ``shake_val``, ``timer``.
    """
    return _keep


def receive(message: str) -> Callable[[F], F]:
    """Пришло сообщение ``broadcast``: ``@event.receive("hello")``."""
    return _keep


def received(message: str) -> Callable[[F], F]:
    """То же, что ``receive``.

    На официальной странице в примере написано ``received``.
    В списке функций и в коде mBlock имя — ``receive``.
    Это написание добавлено для подсказок редактора.
    """
    return _keep


def upload_broadcast(message: str) -> Callable[[F], F]:
    """Пришло сообщение режима Upload."""
    return _keep


def cloud_broadcast(message: str) -> Callable[[F], F]:
    """Пришло облачное сообщение."""
    return _keep


def wifi_broadcast(message: str) -> Callable[[F], F]:
    """Пришло сообщение по локальной сети."""
    return _keep


def mesh_broadcast(message: str) -> Callable[[F], F]:
    """Слушать сообщение Mesh LAN и выполнить код при получении.

    message: имя сообщения, например ``"hello"``.

    На странице API раздел помечен как to be implemented.
    """
    return _keep


__all__ = [
    "start",
    "is_press",
    "is_tiltforward",
    "is_tiltback",
    "is_tiltleft",
    "is_tiltright",
    "is_faceup",
    "is_facedown",
    "is_stand",
    "is_handstand",
    "is_shake",
    "is_waveup",
    "is_wavedown",
    "is_waveleft",
    "is_waveright",
    "is_freefall",
    "is_clockwise",
    "is_anticlockwise",
    "greater_than",
    "smaller_than",
    "receive",
    "received",
    "upload_broadcast",
    "cloud_broadcast",
    "wifi_broadcast",
    "mesh_broadcast",
]
