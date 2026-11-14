"""Сигнатуры библиотеки CyberPi для VS Code.

На CyberPi модуль уже вшит в прошивку. Этот файл нужен редактору:
автодополнение, подсказки и проверка вызовов.
На компьютере функции ничего не делают.

В mBlock заливайте только свою программу. Этот файл на плату копировать
не нужно.

Список функций — со страницы Python API Documentation for CyberPi.
События ``event`` работают только в режиме Upload.

02.11.26 - добавлены все методы и объекты расширения Display+.
14.11.26 - недостающие сигнатуры Function Extension: спрайты, doodle, Mesh LAN.
14.11.26 - уточнены имена аргументов и типы Display+ по странице API.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Literal, TypeVar

import mbot2 as mbot2
import pocket as pocket

F = TypeVar("F", bound=Callable[..., object])

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
ColorAbbrev = Literal["r", "o", "y", "g", "c", "b", "p", "w", "k"]
Color = int | ColorName
SketchColor = Color | ColorAbbrev
LedId = int | Literal["all"]

ButtonName = Literal[
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
]
ButtonCountName = Literal["a", "b", "up", "down", "left", "right", "middle"]
Axis = Literal["x", "y", "z"]
AxisAll = Literal["x", "y", "z", "all"]
EventSource = Literal["microphone", "light_sensor", "shake_val", "timer"]
LoudnessMode = Literal["average", "maximum"]
LabelPos = Literal[
    "center",
    "top_mid",
    "top_left",
    "top_right",
    "mid_left",
    "mid_right",
    "bottom_mid",
    "bottom_left",
    "bottom_right",
]
LedAnim = Literal[
    "rainbow",
    "spoondrift",
    "meteor_blue",
    "meteor_green",
    "flash_red",
    "flash_orange",
    "firefly",
]
DrumType = Literal[
    "snare",
    "bass-drum",
    "side-stick",
    "crash-cymbal",
    "open-hi-hat",
    "closed-hi-hat",
    "tambourine",
    "hand-clap",
    "claves",
]
MusicName = Literal[
    "hello",
    "hi",
    "bye",
    "yeah",
    "wow",
    "laugh",
    "hum",
    "sad",
    "sigh",
    "annoyed",
    "angry",
    "surprised",
    "yummy",
    "curious",
    "embarrassed",
    "ready",
    "sprint",
    "sleepy",
    "meow",
    "start",
    "switch",
    "beeps",
    "buzzing",
    "explosion",
    "jump",
    "laser",
    "level-up",
    "low-energy",
    "prompt-tone",
    "right",
    "wrong",
    "ring",
    "score",
    "wake",
    "warning",
    "metal-clash",
    "shot",
    "glass-clink",
    "inflator",
    "running water",
    "clockwork",
    "click",
    "current",
    "wood-hit",
    "iron",
    "drop",
    "bubble",
    "wave",
    "magic",
    "spitfire",
    "heartbeat",
    "load",
]
WeatherOption = Literal["max_temp", "min_temp", "weather", "humidity"]
AirOption = Literal["aqi", "pm2.5", "pm10", "co", "so2", "no2"]
TimeOption = Literal[
    "sunrise_time",
    "sunrise_hour",
    "sunrise_minute",
    "sunrise_set",
    "sunset_hour",
    "sunset_minute",
    "hour",
    "minute",
    "second",
    "year",
    "month",
    "day",
    "date",
]
CloudLang = Literal[
    "chinese",
    "chinese_taiwan",
    "cantonese",
    "japanese",
    "english",
    "french",
    "german",
    "spanish",
    "portuguese",
    "russian",
    "korean",
    "italian",
    "dutch",
]
SpriteIconName = Literal[
    "Music",
    "Image",
    "Video",
    "Clock",
    "Play",
    "Pause",
    "Next",
    "Prev",
    "Sound",
    "Temperature",
    "Light",
    "Motion",
    "Home",
    "Gear",
    "List",
    "Right",
    "Wrong",
    "Shut_down",
    "Refresh",
    "Trash_can",
    "Download",
    "Sunny",
    "Cloudy",
    "Rain",
    "Snow",
    "Train",
    "Rocket",
    "Truck",
    "Car",
    "Droplet",
    "Distance",
    "Fire",
    "Magnetic",
    "Gas",
    "Vision",
    "Color",
    "Overcast",
    "Sandstorm",
    "Foggy",
    "music",
    "image",
    "video",
    "clock",
    "play",
    "pause",
    "next",
    "prev",
    "sound",
    "temperature",
    "light",
    "motion",
    "home",
    "gear",
    "list",
    "right",
    "wrong",
    "shut_down",
    "refresh",
    "trash_can",
    "download",
    "sunny",
    "cloudy",
    "rain",
    "snow",
    "train",
    "rocket",
    "truck",
    "car",
    "droplet",
    "distance",
    "fire",
    "magnetic",
    "gas",
    "vision",
    "color",
    "overcast",
    "sandstorm",
    "foggy",
]
MirrorAxis = Literal["x", "y"]
SpriteEdge = Literal["edge"]


def _keep(callback: F) -> F:
    return callback


class _Audio:
    @staticmethod
    def play_until(music_name: MusicName) -> None:
        """Проиграть встроенный звук и дождаться конца.

        music_name: ``hello``, ``hi``, ``bye``, ``yeah``, ``wow``, ``laugh``,
        ``hum``, ``sad``, ``sigh``, ``annoyed``, ``angry``, ``surprised``,
        ``yummy``, ``curious``, ``embarrassed``, ``ready``, ``sprint``,
        ``sleepy``, ``meow``, ``start``, ``switch``, ``beeps``, ``buzzing``,
        ``explosion``, ``jump``, ``laser``, ``level-up``, ``low-energy``,
        ``prompt-tone``, ``right``, ``wrong``, ``ring``, ``score``, ``wake``,
        ``warning``, ``metal-clash``, ``shot``, ``glass-clink``, ``inflator``,
        ``running water``, ``clockwork``, ``click``, ``current``, ``wood-hit``,
        ``iron``, ``drop``, ``bubble``, ``wave``, ``magic``, ``spitfire``,
        ``heartbeat``, ``load``.
        """

    @staticmethod
    def play(music_name: MusicName) -> None:
        """Проиграть встроенный звук, не дожидаясь конца."""

    @staticmethod
    def play_music(note: int, beat: float, type: str = "piano") -> None:
        """Сыграть ноту и дождаться конца.

        note: 0–132. beat: длительность в долях, больше 0.

        type: инструмент, по умолчанию ``piano``.
        """

    @staticmethod
    def play_drum(type: DrumType, beat: float) -> None:
        """Сыграть удар и дождаться конца.

        type: ``snare``, ``bass-drum``, ``side-stick``, ``crash-cymbal``,
        ``open-hi-hat``, ``closed-hi-hat``, ``tambourine``, ``hand-clap``,
        ``claves``.

        beat больше 0.
        """

    @staticmethod
    def record() -> None:
        """Начать запись с микрофона. Не дольше 10 секунд, хранится в памяти до выключения."""

    @staticmethod
    def stop_record() -> None:
        """Остановить запись."""

    @staticmethod
    def play_record_until() -> None:
        """Проиграть запись и дождаться конца."""

    @staticmethod
    def play_record() -> None:
        """Проиграть запись, не дожидаясь конца."""

    @staticmethod
    def play_tone(freq: int, t: float) -> None:
        """Пищать с частотой freq герц (20–5000) в течение t секунд."""

    @staticmethod
    def add_tempo(pct: int) -> None:
        """Изменить скорость воспроизведения на pct процентов."""

    @staticmethod
    def set_tempo(pct: int) -> None:
        """Задать скорость воспроизведения, 25–400 процентов."""

    @staticmethod
    def get_tempo() -> int:
        """Текущая скорость воспроизведения, 25–400."""
        return 0

    @staticmethod
    def add_vol(val: int) -> None:
        """Изменить громкость на val процентов, от -100 до 100."""

    @staticmethod
    def set_vol(val: int) -> None:
        """Задать громкость, 0–100 процентов."""

    @staticmethod
    def get_vol() -> int:
        """Текущая громкость, 0–100."""
        return 0

    @staticmethod
    def stop() -> None:
        """Остановить все звуки."""


class _Led:
    @staticmethod
    def on(r: Color, g: int = 0, b: int = 0, id: LedId = "all") -> None:
        """Зажечь светодиоды платы.

        r, g, b: 0–255. В r можно передать имя цвета: ``red``, ``green`` и т.д.

        id: номер 1–5 или ``all``.
        """

    @staticmethod
    def play(name: LedAnim = "rainbow") -> None:
        """Проиграть анимацию и дождаться конца.

        name: ``rainbow``, ``spoondrift``, ``meteor_blue``, ``meteor_green``,
        ``flash_red``, ``flash_orange``, ``firefly``.
        """

    @staticmethod
    def show(color: str) -> None:
        """Задать цвета пяти светодиодов строкой: ``\"r g b y c\"``."""

    @staticmethod
    def move(step: int = 1) -> None:
        """Сдвинуть цвета светодиодов на step позиций, от -4 до 4."""

    @staticmethod
    def off(id: LedId = "all") -> None:
        """Погасить светодиод 1–5 или все (``all``)."""

    @staticmethod
    def add_bri(brightness: int) -> None:
        """Изменить яркость на brightness процентов, от -100 до 100."""

    @staticmethod
    def set_bri(brightness: int) -> None:
        """Задать яркость, 0–100 процентов."""

    @staticmethod
    def get_bri() -> int:
        """Текущая яркость, 0–100."""
        return 0


class _Console:
    @staticmethod
    def print(message: object) -> None:
        """Вывести текст на экран. Перенос, когда строка заполнена."""

    @staticmethod
    def println(message: object) -> None:
        """Вывести текст и перейти на следующую строку."""

    @staticmethod
    def clear() -> None:
        """Очистить консоль экрана.

        В примерах на странице API вызывается ``console.clear()``.
        Отдельного описания параметров у вызова нет.
        """


class _Display:
    @staticmethod
    def show_label(
        message: str,
        size: int,
        x: int | LabelPos = "center",
        y: int = 0,
    ) -> None:
        """Показать надпись.

        size: 16, 24 или 32.

        x: координата 0–128 или позиция ``center``, ``top_mid``, ``top_left``,
        ``top_right``, ``mid_left``, ``mid_right``, ``bottom_mid``,
        ``bottom_left``, ``bottom_right``.

        y: координата 0–128, если x задан числом.
        """

    @staticmethod
    def set_brush(r: Color, g: int = 0, b: int = 0) -> None:
        """Цвет текста и графиков. r, g, b: 0–255, либо имя цвета в r."""

    @staticmethod
    def rotate_to(angle: int) -> None:
        """Повернуть изображение. angle: -180, -90, 0, 90 или 180."""

    @staticmethod
    def clear() -> None:
        """Очистить экран."""

    @staticmethod
    def off() -> None:
        """Выключить подсветку экрана."""


class _Background:
    @staticmethod
    def fill(r: int, g: int, b: int) -> None:
        """Залить весь фон экрана одним цветом RGB (Display+).

        Сейчас многоцветный фон задать нельзя.

        r: красный, 0–255.

        g: зелёный, 0–255.

        b: синий, 0–255.
        """

    @staticmethod
    def copy() -> None:
        """Скопировать всё, что сейчас на экране, в фон (Display+).

        На странице API метод есть, но пока не открыт пользователям.
        """


class _Screen:
    @staticmethod
    def render() -> None:
        """Ручная отрисовка кадра (Display+).

        Координаты, размер и направление спрайта применяются только после
        ``render()`` или автоотрисовки.
        """

    @staticmethod
    def enable_autorender() -> None:
        """Включить автоотрисовку экрана, 10 кадров (Display+)."""

    @staticmethod
    def disable_autorender() -> None:
        """Выключить автоотрисовку. Дальше кадр обновляется через ``render()`` (Display+)."""

    @staticmethod
    def color_get(x: int, y: int) -> str:
        """Цвет пикселя, который сейчас виден на экране (Display+).

        x: координата по горизонтали, 0–127.

        y: координата по вертикали, 0–127.

        Возвращает строку ``"0x000000"`` … ``"0xFFFFFF"``.
        """
        return "0x000000"

    @staticmethod
    def is_color(x: int, y: int) -> int:
        """Цвет пикселя на экране в формате RGB565 (Display+).

        x: координата по горизонтали, 0–127.

        y: координата по вертикали, 0–127.
        """
        return 0

    @staticmethod
    def get_color(x: int, y: int) -> int:
        """Получить цвет пикселя на экране (Display+).

        x: координата по горизонтали, 0–127.

        y: координата по вертикали, 0–127.
        """
        return 0


class _Sketch:
    """Кисть Doodle. По умолчанию: точка (64, 64), толщина 1, цвет белый, не рисует."""

    @staticmethod
    def clear() -> None:
        """Удалить все рисунки кисти на экране (Display+)."""

    @staticmethod
    def start() -> None:
        """Опустить кисть — начать рисование при перемещении (Display+)."""

    @staticmethod
    def end() -> None:
        """Поднять кисть — закончить рисование (Display+)."""

    @staticmethod
    def set_color(r: SketchColor, g: int = 0, b: int = 0) -> None:
        """Задать цвет кисти (Display+).

        r: число 0–255 (красный) или имя/сокращение цвета:
        ``red``/``r``, ``orange``/``o``, ``yellow``/``y``, ``green``/``g``,
        ``cyan``/``c``, ``blue``/``b``, ``purple``/``p``, ``white``/``w``,
        ``black``/``k``.

        g: зелёный, 0–255, если ``r`` — число.

        b: синий, 0–255, если ``r`` — число.
        """

    @staticmethod
    def set_size(size: int) -> None:
        """Задать толщину линии кисти (Display+).

        Наконечник круглый.

        size: толщина в пикселях.
        """

    @staticmethod
    def set_speed(speed: int) -> None:
        """Задать скорость перемещения кисти (Display+).

        speed: скорость, 1–10.
        """

    @staticmethod
    def cw(angle: int) -> None:
        """Повернуть направление кисти по часовой стрелке (Display+).

        angle: угол поворота в градусах.
        """

    @staticmethod
    def ccw(angle: int) -> None:
        """Повернуть направление кисти против часовой стрелки (Display+).

        angle: угол поворота в градусах.
        """

    @staticmethod
    def set_angle(angle: int) -> None:
        """Установить направление, куда смотрит кисть (Display+).

        angle: угол направления в градусах.
        """

    @staticmethod
    def move(step: int) -> None:
        """Переместить кисть вперёд в текущем направлении (Display+).

        step: расстояние в пикселях.
        """

    @staticmethod
    def move_to(x: int, y: int) -> None:
        """Переместить кисть в точку (x, y) на экране (Display+).

        x: координата по горизонтали.

        y: координата по вертикали.
        """

    @staticmethod
    def move_x(step: int) -> None:
        """Сместить кисть слева направо по оси X (Display+).

        step: смещение в пикселях.
        """

    @staticmethod
    def move_y(step: int) -> None:
        """Сместить кисть сверху вниз по оси Y (Display+).

        step: смещение в пикселях.
        """

    @staticmethod
    def circle(r: int, angle: int) -> None:
        """Нарисовать дугу. Центр — перпендикулярно направлению кисти (Display+).

        r: радиус дуги в пикселях.

        angle: угол дуги в градусах.
        """

    @staticmethod
    def get_x() -> int:
        """Текущая координата X кисти (Display+)."""
        return 0

    @staticmethod
    def get_y() -> int:
        """Текущая координата Y кисти (Display+)."""
        return 0

    @staticmethod
    def get_angle() -> int:
        """Угол направления кисти в градусах (Display+)."""
        return 0

    @staticmethod
    def get_size() -> int:
        """Текущая толщина кисти в пикселях (Display+)."""
        return 1

    @staticmethod
    def if_start() -> bool:
        """Кисть опущена и рисует (Display+)."""
        return False


class sprite:
    """Спрайт на экране CyberPi (Display+).

    Создаётся вызовом ``s = cyberpi.sprite()``.

    По умолчанию: точка (64, 64), направление 90°, размер 100%, якорь в центре,
    показан, цвет белый, новый спрайт на верхнем слое.
    """

    def __init__(self) -> None:
        """Создать новый спрайт (Display+)."""

    def pixel_set(self, color: str, x: int, y: int) -> None:
        """Задать цвет одного пикселя спрайта (Display+).

        color: цвет ``"0x000000"`` … ``"0xFFFFFF"``.

        x: координата пикселя, 0–127.

        y: координата пикселя, 0–127.

        На странице API метод есть, но пока не открыт пользователям.
        """

    def draw_pixel(
        self,
        pixel: list[int],
        x_size: int = 16,
        y_size: int = 16,
    ) -> None:
        """Задать изображение спрайта массивом пикселей (Display+).

        pixel: список цветов слева направо и сверху вниз, например
        ``[0xFF0000, 0x00FF00, 0x0000FF]`` — красный, зелёный, синий.

        x_size: ширина узора в пикселях, по умолчанию 16.

        y_size: высота узора в пикселях, по умолчанию 16.

        Цвета за пределами ширины и высоты отбрасываются. Пустые клетки
        считаются прозрачными.
        """

    def draw_icon(self, name: SpriteIconName) -> None:
        """Сделать спрайт встроенной иконкой (Display+).

        name: имя иконки, например ``"music"``, ``"play"``, ``"home"``,
        ``"sunny"``. На странице API метод помечен как to be implemented.
        """

    def draw_text(self, text: str) -> None:
        """Сделать спрайт текстовой надписью (Display+).

        text: строка. Размер шрифта по умолчанию 16 пикселей.

        Поддерживаются китайский, английский, французский, испанский,
        немецкий, итальянский, португальский, русский, корейский, японский
        и нидерландский. Другие языки могут показать кракозябры.
        """

    def draw_QR(self, content: str) -> None:
        """Сделать спрайт QR-кодом (Display+).

        content: строка для кодирования в QR-код.
        """

    def draw_qrcode(self, content: str) -> None:
        """То же, что ``draw_QR``. Имя из примера на странице API (Display+).

        content: строка для кодирования в QR-код.
        """

    def draw_sketch(self) -> sprite:
        """Взять текущий рисунок кисти как изображение этого спрайта (Display+).

        Якорь по умолчанию в точке (64, 64), поэтому эскиз оказывается
        в центре экрана. Возвращает этот же спрайт.
        """
        return self

    def mirror(self, axis: MirrorAxis) -> None:
        """Отразить спрайт зеркально (Display+).

        axis: ``"x"`` — вокруг оси X, то есть сверху вниз;
        ``"y"`` — вокруг оси Y, то есть слева направо.
        """

    def delete(self) -> None:
        """Удалить спрайт с экрана (Display+)."""

    def set_align(self, align_point: LabelPos = "center") -> None:
        """Задать опорную точку (якорь) спрайта (Display+).

        Якорь — центр при движении и повороте.

        align_point: ``"top_mid"``, ``"top_left"``, ``"top_right"``,
        ``"center"``, ``"mid_left"``, ``"mid_right"``, ``"bottom_mid"``,
        ``"bottom_left"`` или ``"bottom_right"``. По умолчанию ``"center"``.
        """

    def move_x(self, step: int) -> None:
        """Сместить спрайт по горизонтали X (Display+).

        step: смещение в пикселях.
        """

    def move_y(self, step: int) -> None:
        """Сместить спрайт по вертикали Y (Display+).

        step: смещение в пикселях.
        """

    def move_to(self, x: int, y: int) -> None:
        """Переместить спрайт в координаты (x, y) (Display+).

        x: координата по горизонтали.

        y: координата по вертикали.
        """

    def move_random(self) -> None:
        """Переместить спрайт в случайную точку. X и Y от 0 до 127 (Display+)."""

    def rotate(self, angle: int) -> None:
        """Повернуть спрайт по часовой стрелке (Display+).

        angle: угол поворота в градусах.
        """

    def rotate_to(self, angle: int = 90) -> None:
        """Повернуть спрайт в указанное направление (Display+).

        angle: направление в градусах, по умолчанию 90°.
        """

    def set_size(self, size: int = 100) -> None:
        """Равномерно масштабировать спрайт в процентах (Display+).

        size: размер в процентах, по умолчанию 100.
        """

    def set_scale(self, x_size: int = 100, y_size: int = 100) -> None:
        """Масштабировать ширину и высоту спрайта по отдельности (Display+).

        x_size: масштаб ширины в процентах, по умолчанию 100.

        y_size: масштаб высоты в процентах, по умолчанию 100.

        На странице API метод есть, но пока не открыт пользователям.
        """

    def set_color(self, r: int, g: int, b: int) -> None:
        """Окрасить все непрозрачные пиксели спрайта фильтром RGB (Display+).

        r: красный, 0–255.

        g: зелёный, 0–255.

        b: синий, 0–255.
        """

    def close_color(self) -> None:
        """Снять цветовой фильтр и вернуть вид из ``draw_XXX()`` (Display+)."""

    def show(self) -> None:
        """Показать спрайт. По умолчанию спрайты уже показаны (Display+)."""

    def hide(self) -> None:
        """Скрыть спрайт с экрана (Display+)."""

    def z_max(self) -> None:
        """Вынести спрайт на передний план (Display+)."""

    def z_min(self) -> None:
        """Убрать спрайт на задний план (Display+)."""

    def z_up(self, step: int) -> None:
        """Поднять спрайт на указанное число слоёв (Display+).

        step: сколько слоёв ближе к зрителю.
        """

    def z_down(self, step: int) -> None:
        """Опустить спрайт на указанное число слоёв (Display+).

        step: сколько слоёв дальше от зрителя.
        """

    def is_touch(self, other_sprite: sprite | SpriteEdge) -> bool:
        """Касается ли спрайт другого спрайта или края экрана (Display+).

        Касание — если непрозрачные пиксели пересеклись. Край экрана — если
        координата непрозрачного пикселя ≥ 128.

        other_sprite: другой ``sprite`` или ``"edge"``.
        """
        return False

    def get_x(self) -> int:
        """Текущая координата X спрайта (Display+)."""
        return 0

    def get_y(self) -> int:
        """Текущая координата Y спрайта (Display+)."""
        return 0

    def get_rotation(self) -> int:
        """Угол, куда смотрит спрайт, от −180° до +180° (Display+)."""
        return 0

    def get_size(self) -> int:
        """Текущий размер спрайта в процентах (Display+)."""
        return 100

    def get_xsize(self) -> int:
        """Масштаб ширины спрайта в процентах (Display+)."""
        return 100

    def get_ysize(self) -> int:
        """Масштаб высоты спрайта в процентах (Display+)."""
        return 100

    def get_align(self) -> str:
        """Текущий якорь спрайта: ``"center"``, ``"top_left"`` и остальные (Display+)."""
        return "center"


class _Chart:
    @staticmethod
    def add(data: float) -> None:
        """Добавить значение на график. Диапазон данных: 0–100."""


class _LineChart(_Chart):
    @staticmethod
    def set_step(step: int) -> None:
        """Шаг между точками линейного графика, 0–128 пикселей."""


class _Table:
    @staticmethod
    def add(row: int, column: int, data: str) -> None:
        """Записать ячейку таблицы. Не больше 4 строк и 3 столбцов."""


class _Controller:
    @staticmethod
    def is_press(name: ButtonName) -> bool:
        """Кнопка или джойстик сейчас нажаты.

        name: ``a``, ``b``, ``up``, ``down``, ``left``, ``right``, ``middle``,
        ``any_direction``, ``any_button``, ``any``.
        """
        return False

    @staticmethod
    def get_count(name: ButtonCountName) -> int:
        """Сколько раз нажали кнопку или сдвинули джойстик.

        name: ``a``, ``b``, ``up``, ``down``, ``left``, ``right``, ``middle``.
        """
        return 0

    @staticmethod
    def reset_count(name: ButtonName) -> None:
        """Сбросить счётчик нажатий.

        name: ``a``, ``b``, ``up``, ``down``, ``left``, ``right``, ``middle``,
        ``any_direction``, ``any_button``, ``any``.
        """


class _Timer:
    @staticmethod
    def get() -> float:
        """Секунды с включения платы или с последнего reset()."""
        return 0.0

    @staticmethod
    def reset() -> None:
        """Обнулить таймер."""


class _Wifi:
    @staticmethod
    def connect(ssid: str, password: str) -> None:
        """Начать подключение к Wi-Fi. Завершение проверяйте через is_connect()."""

    @staticmethod
    def is_connect() -> bool:
        """Wi-Fi уже подключён."""
        return False


class _MessageBus:
    @staticmethod
    def set(message: str, val: str) -> None:
        """Отправить сообщение message со значением val."""

    @staticmethod
    def get(message: str) -> str:
        """Последнее значение сообщения message."""
        return ""


class _Cloud:
    @staticmethod
    def setkey(key: str) -> None:
        """Ключ облака mBlock. Нужен уже подключённый Wi-Fi."""

    @staticmethod
    def weather(option: WeatherOption, woe_id: str) -> str:
        """Погода города woe_id.

        option: ``max_temp``, ``min_temp``, ``weather``, ``humidity``.
        """
        return ""

    @staticmethod
    def air(option: AirOption, woe_id: str) -> str:
        """Воздух города woe_id.

        option: ``aqi``, ``pm2.5``, ``pm10``, ``co``, ``so2``, ``no2``.
        """
        return ""

    @staticmethod
    def time(option: TimeOption, location: str | int) -> str | int:
        """Время или восход/закат.

        option: ``sunrise_time``, ``sunrise_hour``, ``sunrise_minute``,
        ``sunrise_set``, ``sunset_hour``, ``sunset_minute``, ``hour``,
        ``minute``, ``second``, ``year``, ``month``, ``day``, ``date``.

        location: код города или часовой пояс от -12 до 12.
        """
        return ""

    @staticmethod
    def listen(language: CloudLang, t: float | Literal["record"] = 3) -> None:
        """Распознать речь и дождаться результата.

        language: ``chinese``, ``chinese_taiwan``, ``cantonese``, ``japanese``,
        ``english``, ``french``, ``german``, ``spanish``, ``portuguese``,
        ``russian``, ``korean``, ``italian``, ``dutch``.

        t: секунды или ``record``, чтобы взять последнюю запись.
        """

    @staticmethod
    def listen_result() -> str:
        """Последняя распознанная фраза."""
        return ""

    @staticmethod
    def tts(language: CloudLang, message: str) -> None:
        """Произнести message. Сейчас язык выбирается по тексту: китайский или английский."""

    @staticmethod
    def translate(language: CloudLang, message: str) -> str:
        """Перевести message на language. Набор языков тот же, что у listen()."""
        return ""


class _Event:
    @staticmethod
    def start(callback: F) -> F:
        """Поток при запуске CyberPi: ``@cyberpi.event.start``."""
        return _keep(callback)

    @staticmethod
    def is_press(name: ButtonName) -> Callable[[F], F]:
        """Поток при нажатии. name как у controller.is_press."""

        def decorate(callback: F) -> F:
            return callback

        return decorate

    @staticmethod
    def is_tiltforward(callback: F) -> F:
        """Плата наклонилась вперёд."""
        return _keep(callback)

    @staticmethod
    def is_tiltback(callback: F) -> F:
        """Плата наклонилась назад."""
        return _keep(callback)

    @staticmethod
    def is_tiltleft(callback: F) -> F:
        """Плата наклонилась влево."""
        return _keep(callback)

    @staticmethod
    def is_tiltright(callback: F) -> F:
        """Плата наклонилась вправо."""
        return _keep(callback)

    @staticmethod
    def is_faceup(callback: F) -> F:
        """Экран смотрит вверх."""
        return _keep(callback)

    @staticmethod
    def is_facedown(callback: F) -> F:
        """Экран смотрит вниз."""
        return _keep(callback)

    @staticmethod
    def is_stand(callback: F) -> F:
        """Плата стоит светодиодами вниз.

        В истории изменений страницы API это событие добавлено. В текущем
        списке заголовков его нет, рядом есть функция ``is_stand()``.
        """
        return _keep(callback)

    @staticmethod
    def is_handstand(callback: F) -> F:
        """Плата стоит светодиодами вверх.

        В истории изменений страницы API это событие добавлено. В текущем
        списке заголовков его нет, рядом есть функция ``is_handstand()``.
        """
        return _keep(callback)

    @staticmethod
    def is_shake(callback: F) -> F:
        """Плату встряхнули."""
        return _keep(callback)

    @staticmethod
    def is_waveup(callback: F) -> F:
        """Плату взмахнули вверх."""
        return _keep(callback)

    @staticmethod
    def is_wavedown(callback: F) -> F:
        """Плату взмахнули вниз."""
        return _keep(callback)

    @staticmethod
    def is_waveleft(callback: F) -> F:
        """Плату взмахнули влево."""
        return _keep(callback)

    @staticmethod
    def is_waveright(callback: F) -> F:
        """Плату взмахнули вправо."""
        return _keep(callback)

    @staticmethod
    def is_freefall(callback: F) -> F:
        """Плата падает."""
        return _keep(callback)

    @staticmethod
    def is_clockwise(callback: F) -> F:
        """Плата поворачивается по часовой стрелке вокруг оси z."""
        return _keep(callback)

    @staticmethod
    def is_anticlockwise(callback: F) -> F:
        """Плата поворачивается против часовой стрелки вокруг оси z."""
        return _keep(callback)

    @staticmethod
    def greater_than(threshold: int, type: EventSource) -> Callable[[F], F]:
        """Значение стало больше порога 0–100.

        type: ``microphone``, ``light_sensor``, ``shake_val``, ``timer``.
        """

        def decorate(callback: F) -> F:
            return callback

        return decorate

    @staticmethod
    def smaller_than(threshold: int, type: EventSource) -> Callable[[F], F]:
        """Значение стало меньше порога 0–100.

        type: ``microphone``, ``light_sensor``, ``shake_val``, ``timer``.
        """

        def decorate(callback: F) -> F:
            return callback

        return decorate

    @staticmethod
    def receive(message: str) -> Callable[[F], F]:
        """Пришло обычное сообщение broadcast."""

        def decorate(callback: F) -> F:
            return callback

        return decorate

    @staticmethod
    def received(message: str) -> Callable[[F], F]:
        """То же, что receive().

        В примере оформления событий на странице API написано ``received``.
        В списке функций и в сгенерированном коде — ``receive``.
        """

        def decorate(callback: F) -> F:
            return callback

        return decorate

    @staticmethod
    def upload_broadcast(message: str) -> Callable[[F], F]:
        """Пришло сообщение upload-режима."""

        def decorate(callback: F) -> F:
            return callback

        return decorate

    @staticmethod
    def cloud_broadcast(message: str) -> Callable[[F], F]:
        """Пришло облачное сообщение."""

        def decorate(callback: F) -> F:
            return callback

        return decorate

    @staticmethod
    def wifi_broadcast(message: str) -> Callable[[F], F]:
        """Пришло сообщение по локальной сети."""

        def decorate(callback: F) -> F:
            return callback

        return decorate

    @staticmethod
    def mesh_broadcast(message: str) -> Callable[[F], F]:
        """Слушать сообщение Mesh LAN и выполнить код при получении.

        message: имя сообщения, например ``"hello"``.

        На странице API раздел помечен как to be implemented.
        """

        def decorate(callback: F) -> F:
            return callback

        return decorate


class _Mesh:
    @staticmethod
    def set(name: str = "mesh1") -> None:
        """Создать сеть Mesh LAN (Function Extension).

        name: имя сети, по умолчанию ``"mesh1"``.

        На странице API раздел помечен как to be implemented.
        """

    @staticmethod
    def join(name: str = "mesh1") -> None:
        """Подключиться к сети Mesh LAN (Function Extension).

        name: имя сети, по умолчанию ``"mesh1"``.
        """


class _MeshBroadcast:
    @staticmethod
    def set(message: str, val: object) -> None:
        """Отправить широковещательное сообщение Mesh LAN со значением.

        message: имя сообщения.

        val: значение в сообщении.
        """

    @staticmethod
    def get(message: str) -> object:
        """Получить значение из принятого сообщения Mesh LAN.

        message: имя сообщения.

        Возвращает значение, которое передали через ``mesh_broadcast.set``.
        """
        return ""


audio = _Audio()
led = _Led()
console = _Console()
display = _Display()
background = _Background()
screen = _Screen()
sketch = _Sketch()
linechart = _LineChart()
barchart = _Chart()
piechart = _Chart()
table = _Table()
controller = _Controller()
timer = _Timer()
wifi = _Wifi()
wifi_broadcast = _MessageBus()
upload_broadcast = _MessageBus()
cloud_broadcast = _MessageBus()
cloud = _Cloud()
event = _Event()
mesh = _Mesh()
mesh_broadcast = _MeshBroadcast()


def get_bri() -> int:
    """Яркость света вокруг платы, 0–100."""
    return 0


def get_loudness(mode: LoudnessMode = "maximum") -> int:
    """Громкость с микрофона, 0–100.

    mode: ``average`` или ``maximum``.
    """
    return 0


def get_mac_address() -> str:
    """MAC-адрес Wi-Fi, 12 символов. Без подключения значение может быть неверным."""
    return ""


def get_battery() -> int:
    """Заряд аккумулятора Pocket Shield, 0–100 процентов.

    100 — полный заряд. 0 — щит не подключён или батарея разряжена.
    """
    return 0


def get_firmware_version() -> str:
    """Версия прошивки, например ``44.01.001``."""
    return ""


def get_ble() -> str:
    """Имя Bluetooth, например ``Makeblock_LE_XXXXX``."""
    return ""


def get_name() -> str:
    """Имя платы. По умолчанию ``cyberpi``."""
    return ""


def set_name(name: str) -> None:
    """Задать имя платы. Оно видно в CyberOS."""


def get_language() -> str:
    """Язык системы.

    ``chinese``, ``cantonese``, ``japanese``, ``english``, ``french``,
    ``german``, ``spanish``, ``portuguese``, ``russian``, ``korean``,
    ``italian``, ``dutch``.
    """
    return ""


def is_tiltforward() -> bool:
    """Плата наклонена вперёд."""
    return False


def is_tiltback() -> bool:
    """Плата наклонена назад."""
    return False


def is_tiltleft() -> bool:
    """Плата наклонена влево."""
    return False


def is_tiltright() -> bool:
    """Плата наклонена вправо."""
    return False


def is_faceup() -> bool:
    """Экран смотрит вверх."""
    return False


def is_facedown() -> bool:
    """Экран смотрит вниз."""
    return False


def is_stand() -> bool:
    """Плата стоит вертикально, светодиоды снизу."""
    return False


def is_handstand() -> bool:
    """Плата стоит вертикально, светодиоды сверху."""
    return False


def is_shake() -> bool:
    """Плату трясут. Порог силы — 20."""
    return False


def is_waveup() -> bool:
    """Плата взмахнута вверх."""
    return False


def is_wavedown() -> bool:
    """Плата взмахнута вниз."""
    return False


def is_waveleft() -> bool:
    """Плата взмахнута влево."""
    return False


def is_waveright() -> bool:
    """Плата взмахнута вправо."""
    return False


def is_freefall() -> bool:
    """Плата в свободном падении."""
    return False


def is_clockwise() -> bool:
    """Плата вращается по часовой стрелке вокруг оси z."""
    return False


def is_anticlockwise() -> bool:
    """Плата вращается против часовой стрелки вокруг оси z."""
    return False


def get_shakeval() -> int:
    """Сила тряски, 0–100."""
    return 0


def get_wave_angle() -> int:
    """Направление взмаха, от -179 до 180 градусов."""
    return 0


def get_wave_speed() -> int:
    """Скорость взмаха, 0–100. Это не скорость в метрах в секунду."""
    return 0


def get_pitch() -> int:
    """Тангаж: угол оси y к горизонту, от -90 до 90 градусов."""
    return 0


def get_roll() -> int:
    """Крен: угол оси x к горизонту, от -179 до 180 градусов."""
    return 0


def get_yaw() -> int:
    """Рыскание вокруг оси z, от -180 до 180 градусов. Накапливает ошибку."""
    return 0


def reset_yaw() -> None:
    """Обнулить рыскание."""


def get_acc(axis: Axis) -> float:
    """Ускорение по оси ``x``, ``y`` или ``z``, м/с²."""
    return 0.0


def get_gyro(axis: Axis) -> int:
    """Угловая скорость вокруг оси ``x``, ``y`` или ``z``, от -500 до 500 °/с."""
    return 0


def get_rotation(axis: Axis) -> float:
    """Угол поворота вокруг оси ``x``, ``y`` или ``z``. Плюс — против часовой."""
    return 0.0


def reset_rotation(axis: AxisAll = "all") -> None:
    """Обнулить угол поворота. axis: ``x``, ``y``, ``z`` или ``all``."""


def broadcast(message: str) -> None:
    """Отправить сообщение другим потокам на плате."""


def stop_all() -> None:
    """Остановить все сценарии."""


def stop_this() -> None:
    """Остановить текущий сценарий."""


def stop_other() -> None:
    """Остановить все сценарии, кроме текущего."""


def restart() -> None:
    """Перезапустить CyberPi."""


__all__ = [
    "audio",
    "led",
    "console",
    "display",
    "background",
    "screen",
    "sketch",
    "sprite",
    "linechart",
    "barchart",
    "piechart",
    "table",
    "controller",
    "timer",
    "wifi",
    "wifi_broadcast",
    "upload_broadcast",
    "cloud_broadcast",
    "cloud",
    "event",
    "mesh",
    "mesh_broadcast",
    "mbot2",
    "pocket",
    "get_bri",
    "get_loudness",
    "get_mac_address",
    "get_battery",
    "get_firmware_version",
    "get_ble",
    "get_name",
    "set_name",
    "get_language",
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
    "get_shakeval",
    "get_wave_angle",
    "get_wave_speed",
    "get_pitch",
    "get_roll",
    "get_yaw",
    "reset_yaw",
    "get_acc",
    "get_gyro",
    "get_rotation",
    "reset_rotation",
    "broadcast",
    "stop_all",
    "stop_this",
    "stop_other",
    "restart",
]
