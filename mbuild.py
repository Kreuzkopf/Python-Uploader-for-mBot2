"""Сигнатуры библиотеки mBuild для VS Code.

На CyberPi модуль ``mbuild`` уже вшит в прошивку. Этот файл нужен редактору.
На компьютере функции ничего не делают.

В mBlock заливайте только свою программу. Этот файл на плату копировать
не нужно.

У всех вызовов есть ``index``: номер модуля среди одинаковых. Один модуль —
это 1, параметр можно не писать.

25.10.26 - актуализирован класс _QuadRgb, учтены методы mBlock5 web.
"""

from __future__ import annotations
from typing import overload, Literal

Channel = int | Literal["any"]
Index = int | Literal["all"]
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


class _Button:
    @staticmethod
    def is_press(index: int = 1) -> bool:
        """Кнопка модуля нажата."""
        return False

    @staticmethod
    def get_count(index: int = 1) -> int:
        """Сколько раз нажали кнопку после включения."""
        return 0

    @staticmethod
    def reset_count(index: int = 1) -> None:
        """Обнулить счётчик нажатий."""


class _AngleSensor:
    @staticmethod
    def get(index: int = 1) -> float:
        """Угол от положения при включении. Плюс — по часовой стрелке."""
        return 0.0

    @staticmethod
    def reset(index: int = 1) -> None:
        """Сбросить накопленный угол."""

    @staticmethod
    def get_speed(index: int = 1) -> float:
        """Скорость вращения, градусы в секунду. Плюс — по часовой."""
        return 0.0

    @staticmethod
    def is_clockwise(index: int = 1) -> bool:
        """Датчик крутится по часовой стрелке."""
        return False

    @staticmethod
    def is_anticlockwise(index: int = 1) -> bool:
        """Датчик крутится против часовой стрелки."""
        return False


class _Slider:
    @staticmethod
    def get(index: int = 1) -> float:
        """Положение ползунка, 0–100 процентов."""
        return 0.0


class _Joystick:
    @staticmethod
    def get_x(index: int = 1) -> float:
        """Отклонение джойстика по оси x, от -100 до 100."""
        return 0.0

    @staticmethod
    def get_y(index: int = 1) -> float:
        """Отклонение джойстика по оси y, от -100 до 100."""
        return 0.0

    @staticmethod
    def is_up(index: int = 1) -> bool:
        """Джойстик отклонён вверх."""
        return False

    @staticmethod
    def is_down(index: int = 1) -> bool:
        """Джойстик отклонён вниз."""
        return False

    @staticmethod
    def is_left(index: int = 1) -> bool:
        """Джойстик отклонён влево."""
        return False

    @staticmethod
    def is_right(index: int = 1) -> bool:
        """Джойстик отклонён вправо."""
        return False


class _MultiTouch:
    @staticmethod
    def is_touch(ch: Channel = "any", index: int = 1) -> bool:
        """Площадка ch касается. ``any`` или номер 1–8."""
        return False

    @staticmethod
    def reset(level: Literal["low", "middle", "high"] = "middle", index: int = 1) -> None:
        """Чувствительность: ``low``, ``middle`` или ``high``."""


class _Science:
    @staticmethod
    def pir_is_active(index: int = 1) -> bool:
        """Датчик движения PIR видит человека или животное."""
        return False

    @staticmethod
    def flame_is_active(index: int = 1) -> bool:
        """Датчик пламени видит огонь."""
        return False

    @staticmethod
    def flame_get(index: int = 1) -> int:
        """Уровень сигнала датчика пламени."""
        return 0

    @staticmethod
    def soil_get(index: int = 1) -> int:
        """Влажность почвы."""
        return 0

    @staticmethod
    def soil_get_resistance(index: int = 1) -> int:
        """Сопротивление между щупами почвы, кОм."""
        return 0

    @staticmethod
    def soil_get_adc_value(index: int = 1) -> int:
        """Сырое значение АЦП датчика почвы."""
        return 0

    @staticmethod
    def mq2_is_active(index: int = 1) -> bool:
        """Датчик MQ2 видит горючий газ."""
        return False

    @staticmethod
    def mq2_get(index: int = 1) -> int:
        """Концентрация горючего газа с MQ2."""
        return 0

    @staticmethod
    def mq2_on(threshold: float, index: int = 1) -> None:
        """Включить MQ2. threshold — чувствительность от 0.1 до 1.0."""

    @staticmethod
    def mq2_off(index: int = 1) -> None:
        """Выключить MQ2."""

    @staticmethod
    def touch_get_resistance(index: int = 1) -> int:
        """Сопротивление точки касания, кОм."""
        return 0

    @staticmethod
    def touch_get_adc_value(index: int = 1) -> int:
        """Сырое значение АЦП точки касания."""
        return 0

    @staticmethod
    def humiture_get_temp(index: int = 1) -> float:
        """Температура с датчика влажности, градусы Цельсия."""
        return 0.0

    @staticmethod
    def humiture_get_humidity(index: int = 1) -> int:
        """Влажность воздуха, проценты."""
        return 0

    @staticmethod
    def compass_get(axis: Literal["x", "y", "z"], index: int = 1) -> int:
        """Магнитный поток по оси ``x``, ``y`` или ``z``."""
        return 0

    @staticmethod
    def compass_get_angle(index: int = 1) -> int:
        """Угол компаса."""
        return 0

    @staticmethod
    def compass_reset(switch: int, index: int = 1) -> None:
        """Калибровка компаса: 1 включить, 0 выключить."""

    @staticmethod
    def compass_is_active(index: int = 1) -> bool:
        """Рядом есть магнит."""
        return False

    @staticmethod
    def atmos_get(index: int = 1) -> int:
        """Атмосферное давление."""
        return 0

    @staticmethod
    def atmos_get_altitude(index: int = 1) -> int:
        """Высота, оцененная по давлению."""
        return 0


class _QuadRgb:

    @staticmethod
    def get_line_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую цвету лини.

        Биты слева направо, старший — левый сенсор. Значения бита ``0`` — фон, ``1`` — линия.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_line_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_line_sta("middle", index)`` — только L1 и R1, возвращает число 0–3.

        ``get_line_sta(index)`` — без указания position работает как get_ground_sta("all", index)."""
        return 0

    @staticmethod
    def get_ground_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую цвету фону.

        Биты слева направо, старший — левый сенсор. Значения бита ``0`` — линия, ``1`` — фон.
                
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_ground_sta("all", index)`` — четыре сенсора, возвращает число 0–15.

        ``get_ground_sta("middle", index)`` — только L1 и R1, возвращает число 0–3."""
        return 0
    
    @staticmethod
    def get_white_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую белому цвету.

        Биты слева направо, старший — левый сенсор. 
        Значения бита ``0`` — не белый цвет, ``1`` — белый цвет.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_white_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_white_sta("middle", index)`` — только L1 и R1, возвращает число 0–3."""
        return 0
   
    @staticmethod
    def get_red_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую красному цвету.

        Биты слева направо, старший — левый сенсор. 
        Значения бита ``0`` — не красный цвет, ``1`` — красный цвет.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_red_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_red_sta("middle", index)`` — только L1 и R1, возвращает число 0–3."""
        return 0
        
    @staticmethod
    def get_yellow_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую желтому цвету.

        Биты слева направо, старший — левый сенсор. 
        Значения бита ``0`` — не желтый цвет, ``1`` — желтый цвет.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_yellow_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_yellow_sta("middle", index)`` — только L1 и R1, возвращает число 0–3."""
        return 0
                      
    @staticmethod
    def get_green_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую зеленому цвету.

        Биты слева направо, старший — левый сенсор. 
        Значения бита ``0`` — не зеленый цвет, ``1`` — зеленый цвет.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_green_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_green_sta("middle", index)`` — только L1 и R1, возвращает число 0–3."""
        return 0

    @staticmethod
    def get_cyan_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую голубому цвету.

        Биты слева направо, старший — левый сенсор. 
        Значения бита ``0`` — не голубой цвет, ``1`` — голубой цвет.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_cyan_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_cyan_sta("middle", index)`` — только L1 и R1, возвращает число 0–3."""
        return 0

    @staticmethod
    def get_blue_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую синему цвету.

        Биты слева направо, старший — левый сенсор. 
        Значения бита ``0`` — не синий цвет, ``1`` — синий цвет.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_blue_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_blue_sta("middle", index)`` — только L1 и R1, возвращает число 0–3."""
        return 0

    @staticmethod
    def get_purple_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую фиолетовому цвету.

        Биты слева направо, старший — левый сенсор. 
        Значения бита ``0`` — не фиолетовый цвет, ``1`` — фиолетовый цвет.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_purple_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_purple_sta("middle", index)`` — только L1 и R1, возвращает число 0–3."""
        return 0

    @staticmethod
    def get_black_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую черному цвету.

        Биты слева направо, старший — левый сенсор. 
        Значения бита ``0`` — не черный цвет, ``1`` — черный цвет.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_black_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_black_sta("middle", index)`` — только L1 и R1, возвращает число 0–3."""
        return 0

    @staticmethod
    def get_custom_sta(
        position: Literal["middle", "all"], index: int = 1) -> int:
        """Возвращает битовую маску четырёх или двух сенсоров, соответствующую пользовательскому цвету.

        Биты слева направо, старший — левый сенсор. 
        Значения бита ``0`` — не пользовательский цвет, ``1`` — пользовательский цвет.
        
        position: ``all`` - L2 L1 R1 R2, ``middle`` - L1 R1.

        ``get_custom_sta("all", index)`` — четыре сенсора, возвращает число 0–15.
        
        ``get_custom_sta("middle", index)`` — только L1 и R1, возвращает число 0–3.
        
        По умолчанию - цвет линии."""
        return 0
                                    
    @staticmethod
    def color_mode(mode: Literal["standard", "enhance"]) -> None:
        """Режим распознавания цвета датчика QuadRGB.

        Датчик сравнивает цвет по тону, насыщенности и яркости.

        ``standard`` — пороги из прежней прошивки. Так датчик
        работает, пока этот метод не вызывали.

        ``enhance`` — усиленный режим новой прошивки. Пороги
        подстраиваются под освещение и поверхность, поэтому
        близкие цвета различаются увереннее.

        Вернуть обычный режим: ``color_mode("standard")``.
        Если вызов убрать из программы, прежний режим включится
        после выключения и включения CyberPi.
        """
        return 0

    @staticmethod
    def get_offset_track(index: int = 1) -> int:
        """Смещение с линии, от -100 до 100. -100 — датчик левее линии."""
        return 0

    @staticmethod
    def is_line(ch: Literal["any", "L2", "L1", "R1", "R2"], index: int = 1) -> bool:
        """Сенсор читает линию.

        ch: ``any``, ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1.
        
        Возвращает логическое значение:
        True: обнаружено
        False: не обнаружено."""
        return False

    @staticmethod
    def is_background(
        ch: Literal["any", "L2", "L1", "R1", "R2"], index: int = 1
    ) -> bool:
        """Сенсор читает фон.
        
        ch: ``any``, ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1.
        
        Возвращает логическое значение:
        True: обнаружено
        False: не обнаружено."""
        return False

    @staticmethod
    def is_color(
        color: Literal[
            "red", "yellow", "green", "cyan", "blue", "purple", "white", "black"
        ],
        ch: Literal["any", "L2", "L1", "R1", "R2"],
        index: int = 1,
    ) -> bool:
        """Сенсор читает цвет.

        color: ``red``, ``yellow``, ``green``, ``cyan``, ``blue``, ``purple``,
        ``white``, ``black``.

        ch: ``any``, ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1.

        Возвращает логическое значение:
        True: обнаружено
        False: не обнаружено."""
        return False

    @staticmethod
    def get_red(ch: Literal["L2", "L1", "R1", "R2"], index: int = 1) -> int:
        """Сенсор измеряет красную составляющую цвета, возвращает от 0 до 255.

        ch: ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1."""
        return 0

    @staticmethod
    def get_green(ch: Literal["L2", "L1", "R1", "R2"], index: int = 1) -> int:
        """Сенсор измеряет зеленую составляющую цвета, возвращает от 0 до 255.

        ch: ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1."""
        return 0

    @staticmethod
    def get_blue(ch: Literal["L2", "L1", "R1", "R2"], index: int = 1) -> int:
        """Сенсор измеряет синюю составляющую цвета, возвращает от 0 до 255.

        ch: ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1."""
        return 0

    @staticmethod
    def get_gray(ch: Literal["L2", "L1", "R1", "R2"], index: int = 1) -> int:
        """Сенсор измеряет уровень отражения цвета в градациях серого, возвращает от 0 до 100.

        ch: ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1.
        
        Значение 0 соотвствует черному цвету, значение 100 - белому."""
        return 0

    @staticmethod
    def get_color(ch: Literal["L2", "L1", "R1", "R2"], index: int = 1) -> int:
        """Сенсор читает цвет. Возвращает hex число от 0x000000 до 0xFFFFFF.

        ch: ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1."""
        return 0

    @staticmethod
    def get_color_sta(ch: Literal["L2", "L1", "R1", "R2"], index: int = 1) -> str:
        """Сенсор читает цвет. Возвращает имя: red, yellow, green, cyan, blue, purple, white, black.

        ch: ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1."""
        return ""

    @staticmethod
    def get_light(ch: Literal["L2", "L1", "R1", "R2"], index: int = 1) -> int:
        """Сенсор измеряет освещенность, возвращает от 0 до 100.

        ch: ``L2``, ``L1``, ``R1``, ``R2`` или 4, 3, 2, 1.
        
        Значение 0 соотвствует минимальной освещенности, значение 100 - максимальной.
        Подсветка тоже считается светом. При необходимости может быть отключена."""
        return 0

    @staticmethod
    def set_led(
        color: Literal[
            "red", "yellow", "green", "cyan", "blue", "purple", "white", "black"
        ],
        index: int = 1,
    ) -> None:
        """Цвет подсветки: имя цвета.

        Состояние сохраняется при использовании метода get_ligth().
        Подсветка не удерживаются при использовании методов измерения цвета поля, 
        заполняющий свет устанавливается из последнего состояния set_led_color().

        color: ``red``, ``yellow``, ``green``, ``cyan``, ``blue``, ``purple``,
        ``white``, ``black``.

        Цвет ``black`` выключает подсветку аналогично методу off_led() или close_led().
        """

    @staticmethod
    def set_led_color(color: Literal["red", "green", "blue"], index: int = 1) -> None:
        """Цвет подсветки: имя.

        color: ``red``, ``green``, ``blue``."""

    @staticmethod
    def set_custom_color(red: int, green: int, blue: int, tolerance: int, index: int = 1) -> None:
        """Задает пользовательский цвет.

        red: красная составляющая цвета от 0 до 255.
        
        green: зеленая составляющая цвета от 0 до 255
        
        blue: синяя составляющая цвета от 0 до 255
        
        tolerance: допустимое отклонение от 0 до 255
        
        Допустимое отклонение применяется к red, green, blue.
        Позволяет расширить диапазон распознавания цвета."""        

    @staticmethod
    def off_led(index: int = 1) -> None:
        """Выключает подсветку.
        
        Состояние сохраняется при использовании метода get_ligth().
        Подсветка не удерживаются при использовании методов измерения цвета поля, 
        заполняющий свет устанавливается из последнего состояния set_led_color().

        Аналогично методу close_led()."""

    @staticmethod
    def close_led(index: int = 1) -> None:
        """Выключает подсветку.
        
        Состояние сохраняется при использовании метода get_ligth().
        Подсветка не удерживаются при использовании методов измерения цвета поля, 
        заполняющий свет устанавливается из последнего состояния set_led_color().

        Аналогично методу off_led()."""

    @staticmethod
    def adjust(index: int = 1) -> None:
        """Калибровка датчика.
        
        После выполнения на экране появится надпись "Calibration completed"."""

class _Ultrasonic2:
    @staticmethod
    def get(index: int = 1) -> float:
        """Расстояние до препятствия, 3–300 см, погрешность около 5 процентов."""
        return 0.0

    @staticmethod
    def led_show(bri: list[int], index: int = 1) -> None:
        """Яркость восьми светодиодов списком из восьми чисел."""

    @staticmethod
    def set_bri(led_bri: float, id: Index = "all", index: int = 1) -> None:
        """Яркость светодиода 0–100. id: 1–8 или ``all``."""

    @staticmethod
    def add_bri(led_bri: float, id: Index = "all", index: int = 1) -> None:
        """Прибавить яркость, 0–100. id: 1–8 или ``all``."""

    @staticmethod
    def get_bri(id: Index, index: int = 1) -> float:
        """Яркость светодиода. id: 1–8 или ``all``."""
        return 0.0

    @staticmethod
    def play(emotion: Literal["sleepy", "happy", "dizzy", "wink", "thinking"], index: int = 1) -> None:
        """Показать эмоцию светодиодами и дождаться конца.

        emotion: ``sleepy``, ``happy``, ``dizzy``, ``wink``, ``thinking``.
        В документации вызов помечен как ещё не реализованный.
        """


class _LightSensor:
    @staticmethod
    def get(index: int = 1) -> float:
        """Освещённость, 0–100."""
        return 0.0


class _DualRgb:
    @staticmethod
    def is_color(
        color: Literal[
            "red", "yellow", "green", "cyan", "blue", "purple", "white", "black"
        ] = "white",
        ch: int = 1,
        index: int = 1,
    ) -> bool:
        """Сенсор ch (1 или 2) видит цвет. Имена цветов как у Quad RGB."""
        return False

    @staticmethod
    def get_red(ch: int = 1, index: int = 1) -> int:
        """Красная составляющая, 0–255. ch: 1 или 2."""
        return 0

    @staticmethod
    def get_green(ch: int = 1, index: int = 1) -> int:
        """Зелёная составляющая, 0–255."""
        return 0

    @staticmethod
    def get_blue(ch: int = 1, index: int = 1) -> int:
        """Синяя составляющая, 0–255."""
        return 0

    @staticmethod
    def get_light(ch: int = 1, index: int = 1) -> int:
        """Освещённость, 0–100."""
        return 0

    @staticmethod
    def get_gray_level(ch: int = 1, index: int = 1) -> int:
        """Отражённый свет, 0–100."""
        return 0

    @staticmethod
    def set_led(
        color: Literal[
            "red", "yellow", "green", "cyan", "blue", "purple", "white", "black"
        ] = "white",
        index: int = 1,
    ) -> None:
        """Цвет подсветки."""

    @staticmethod
    def off_led(index: int = 1) -> None:
        """Выключить подсветку."""


class _SoundSensor:
    @staticmethod
    def get(index: int = 1) -> float:
        """Громкость, 0–100."""
        return 0.0


class _Pir:
    @staticmethod
    def is_detect(index: int = 1) -> bool:
        """PIR видит движение. Срабатывание держится около трёх секунд."""
        return False

    @staticmethod
    def get_count(index: int = 1) -> int:
        """Сколько раз PIR сработал после включения."""
        return 0

    @staticmethod
    def reset_count(index: int = 1) -> None:
        """Обнулить счётчик PIR."""


class _Ultrasonic:
    @staticmethod
    def get(index: int = 1) -> float:
        """Расстояние старого ультразвукового датчика, 3–300 см."""
        return 0.0


class _RangingSensor:
    @staticmethod
    def get(index: int = 1) -> float:
        """Расстояние дальномера, 2–200 см."""
        return 0.0


class _MotionSensor:
    @staticmethod
    def is_shake(index: int = 1) -> bool:
        """Датчик трясут."""
        return False

    @staticmethod
    def get_shakeval(index: int = 1) -> float:
        """Сила тряски, 0–100."""
        return 0.0

    @staticmethod
    def get_accel(axis: Literal["x", "y", "z"], index: int = 1) -> float:
        """Ускорение по оси ``x``, ``y`` или ``z``, м/с²."""
        return 0.0

    @staticmethod
    def is_tiltleft(index: int = 1) -> bool:
        """Наклон влево больше 15 градусов."""
        return False

    @staticmethod
    def is_tiltright(index: int = 1) -> bool:
        """Наклон вправо больше 15 градусов."""
        return False

    @staticmethod
    def is_tiltup(index: int = 1) -> bool:
        """Наклон вверх больше 15 градусов."""
        return False

    @staticmethod
    def is_tiltdown(index: int = 1) -> bool:
        """Наклон вниз больше 15 градусов."""
        return False

    @staticmethod
    def is_faceup(index: int = 1) -> bool:
        """Лежит лицом вверх."""
        return False

    @staticmethod
    def is_facedown(index: int = 1) -> bool:
        """Лежит лицом вниз."""
        return False

    @staticmethod
    def get_roll(index: int = 1) -> float:
        """Крен, от -90 до 90 градусов."""
        return 0.0

    @staticmethod
    def get_pitch(index: int = 1) -> float:
        """Тангаж, от -180 до 180 градусов."""
        return 0.0

    @staticmethod
    def get_yaw(index: int = 1) -> float:
        """Рыскание, 0–360 градусов. Без компаса накапливает ошибку."""
        return 0.0

    @staticmethod
    def get_gyro(axis: Literal["x", "y", "z"], index: int = 1) -> float:
        """Угловая скорость вокруг ``x``, ``y`` или ``z``, градусы в секунду."""
        return 0.0

    @staticmethod
    def get_rotation(axis: Literal["x", "y", "z"], index: int = 1) -> float:
        """Угол поворота вокруг оси. Плюс — против часовой стрелки."""
        return 0.0

    @staticmethod
    def reset_rotation(axis: Literal["x", "y", "z", "all"] = "all", index: int = 1) -> None:
        """Обнулить угол. axis: ``x``, ``y``, ``z`` или ``all``."""


class _SoilSensor:
    @staticmethod
    def get(index: int = 1) -> float:
        """Влажность почвы, 0–100."""
        return 0.0


class _TempSensor:
    @staticmethod
    def get(index: int = 1) -> float:
        """Температура, от -55 до 125 °C."""
        return 0.0


class _Humiture:
    @staticmethod
    def get_humidity(index: int = 1) -> float:
        """Влажность воздуха, 0–100 процентов."""
        return 0.0

    @staticmethod
    def get_temp(index: int = 1) -> float:
        """Температура, от -40 до 125 °C."""
        return 0.0


class _Mq2:
    @staticmethod
    def is_detect(level: Literal["high", "low"] = "high", index: int = 1) -> bool:
        """Газ выше порога. level: ``high`` или ``low``."""
        return False

    @staticmethod
    def get(index: int = 1) -> float:
        """Концентрация газа, 0–100."""
        return 0.0


class _FlameSensor:
    @staticmethod
    def is_detect(index: int = 1) -> bool:
        """Пламя обнаружено."""
        return False

    @staticmethod
    def get(index: int = 1) -> float:
        """Уровень пламени, 0–100."""
        return 0.0


class _MagneticSensor:
    @staticmethod
    def is_detect(index: int = 1) -> bool:
        """Рядом магнит."""
        return False

    @staticmethod
    def get_count(index: int = 1) -> int:
        """Сколько раз магнит сработал после включения."""
        return 0

    @staticmethod
    def reset_count(index: int = 1) -> None:
        """Обнулить счётчик магнита."""


class _SmartCamera:
    @staticmethod
    def set_mode(mode: Literal["color", "line"] = "color", index: int = 1) -> None:
        """Режим: ``color`` — цветные блоки, ``line`` — линия и штрихкоды."""

    @staticmethod
    def learn(sign: int = 1, t: float | Literal["until_button"] = "until_button", index: int = 1) -> None:
        """Выучить цветовой блок 1–7.

        t: секунды или ``until_button``. Вызов ждёт конца обучения.
        """

    @staticmethod
    def detect_sign(sign: int, index: int = 1) -> bool:
        """Цветовой блок 1–7 виден в кадре."""
        return False

    @staticmethod
    def detect_sign_location(
        sign: int,
        location: Literal["up", "down", "left", "right", "middle"],
        index: int = 1,
    ) -> bool:
        """Блок виден в зоне ``up``, ``down``, ``left``, ``right`` или ``middle``."""
        return False

    @staticmethod
    def get_sign_x(sign: int, index: int = 1) -> int:
        """Координата x блока, 0–319. Нет блока — 0."""
        return 0

    @staticmethod
    def get_sign_y(sign: int, index: int = 1) -> int:
        """Координата y блока, 0–239. Нет блока — 0."""
        return 0

    @staticmethod
    def get_sign_wide(sign: int, index: int = 1) -> int:
        """Ширина блока, 0–319."""
        return 0

    @staticmethod
    def get_sign_hight(sign: int, index: int = 1) -> int:
        """Высота блока, 0–239. Имя в API написано как hight."""
        return 0

    @staticmethod
    def open_light(index: int = 1) -> None:
        """Включить две подсветки камеры."""

    @staticmethod
    def close_light(index: int = 1) -> None:
        """Выключить подсветку камеры."""

    @staticmethod
    def reset(index: int = 1) -> None:
        """Сбросить баланс белого. Вызов занимает около пяти секунд."""

    @staticmethod
    def detect_label(label: int, index: int = 1) -> bool:
        """Штрихкод 1–15 виден в кадре."""
        return False

    @staticmethod
    def get_label_x(label: int, index: int = 1) -> int:
        """Координата x штрихкода, 0–319."""
        return 0

    @staticmethod
    def get_label_y(label: int, index: int = 1) -> int:
        """Координата y штрихкода, 0–239."""
        return 0

    @staticmethod
    def detect_cross(index: int = 1) -> bool:
        """В кадре есть перекрёсток."""
        return False

    @staticmethod
    def get_cross_x(index: int = 1) -> int:
        """Координата x перекрёстка, 0–319."""
        return 0

    @staticmethod
    def get_cross_y(index: int = 1) -> int:
        """Координата y перекрёстка, 0–239."""
        return 0

    @staticmethod
    def get_cross_road(index: int = 1) -> int:
        """Сколько перекрёстков видно."""
        return 0

    @staticmethod
    def get_cross_angle(sn: int = 1, index: int = 1) -> float:
        """Угол перекрёстка номер sn относительно вектора камеры."""
        return 0.0

    @staticmethod
    def set_line(mode: Literal["black", "white"] = "black", index: int = 1) -> None:
        """Какую линию искать: ``black`` или ``white``."""

    @staticmethod
    def get_vector_start_x(index: int = 1) -> int:
        """Начало вектора линии, x, 0–319."""
        return 0

    @staticmethod
    def get_vector_start_y(index: int = 1) -> int:
        """Начало вектора линии, y, 0–239."""
        return 0

    @staticmethod
    def get_vector_end_x(index: int = 1) -> int:
        """Конец вектора линии, x, 0–319."""
        return 0

    @staticmethod
    def get_vector_end_y(index: int = 1) -> int:
        """Конец вектора линии, y, 0–239."""
        return 0

    @staticmethod
    def set_vector_angle(angle: float, index: int = 1) -> None:
        """Предпочтительный угол следующего вектора на перекрёстке."""

    @staticmethod
    def get_vector_angle(index: int = 1) -> float:
        """Заданный угол вектора, от -180 до 180 градусов."""
        return 0.0

    @staticmethod
    def set_kp(kp: float, index: int = 1) -> None:
        """Коэффициент Kp для расчёта разницы скоростей моторов."""

    @staticmethod
    def get_sign_diff_speed(
        sign: int,
        axis: Literal["x", "y"],
        axis_val: float,
        index: int = 1,
    ) -> float:
        """Разница скоростей, чтобы удержать блок sign на оси x или y. Результат 0–100."""
        return 0.0

    @staticmethod
    def get_label_diff_speed(
        label: int,
        axis: Literal["x", "y"],
        axis_val: float,
        index: int = 1,
    ) -> float:
        """Разница скоростей, чтобы удержать штрихкод. Результат 0–100."""
        return 0.0

    @staticmethod
    def get_follow_vector_diff_speed(index: int = 1) -> float:
        """Разница скоростей, чтобы держать линию в центре. Результат 0–100."""
        return 0.0

    @staticmethod
    def is_lock_sign(sign: int, axis: Literal["x", "y"], axis_val: float, index: int = 1) -> bool:
        """Блок уже рядом с заданной координатой оси x или y."""
        return False

    @staticmethod
    def is_lock_label(label: int, axis: Literal["x", "y"], axis_val: float, index: int = 1) -> bool:
        """Штрихкод уже рядом с заданной координатой оси x или y."""
        return False


class _LedMatrix:
    @staticmethod
    def show(image: str | int = "hi", index: int = 1) -> None:
        """Картинка: имя вроде ``hi`` или 32-значное шестнадцатеричное поле 16×8."""

    @staticmethod
    def print(message: str, index: int = 1) -> None:
        """Прокрутить текст. Китайские символы не поддерживаются."""

    @staticmethod
    def print_until_done(message: str, index: int = 1) -> None:
        """Прокрутить текст и дождаться конца."""

    @staticmethod
    def print_at(message: str, x: int, y: int, index: int = 1) -> None:
        """Текст с точки x 0–15, y 0–7."""

    @staticmethod
    def on(x: int, y: int, index: int = 1) -> None:
        """Зажечь точку. x 0–15, y 0–7."""

    @staticmethod
    def off(x: int, y: int, index: int = 1) -> None:
        """Погасить точку."""

    @staticmethod
    def toggle(x: int, y: int, index: int = 1) -> None:
        """Переключить точку."""

    @staticmethod
    def clear(index: int = 1) -> None:
        """Погасить всю матрицу."""


class _RgbLed:
    @staticmethod
    def on(r: int | ColorName, g: int = 0, b: int = 0, index: int = 1) -> None:
        """Цвет светодиода. r, g, b: 0–255, либо имя цвета в r."""

    @staticmethod
    def off(index: int = 1) -> None:
        """Выключить светодиод."""

    @staticmethod
    def set_red(val: int, index: int = 1) -> None:
        """Красный канал, 0–255."""

    @staticmethod
    def set_green(val: int, index: int = 1) -> None:
        """Зелёный канал, 0–255."""

    @staticmethod
    def set_blue(val: int, index: int = 1) -> None:
        """Синий канал, 0–255."""

    @staticmethod
    def add_red(val: int, index: int = 1) -> None:
        """Прибавить красный, от -255 до 255."""

    @staticmethod
    def add_green(val: int, index: int = 1) -> None:
        """Прибавить зелёный, от -255 до 255."""

    @staticmethod
    def add_blue(val: int, index: int = 1) -> None:
        """Прибавить синий, от -255 до 255."""

    @staticmethod
    def get_red(index: int = 1) -> int:
        """Текущий красный канал, 0–255."""
        return 0

    @staticmethod
    def get_green(index: int = 1) -> int:
        """Текущий зелёный канал, 0–255."""
        return 0

    @staticmethod
    def get_blue(index: int = 1) -> int:
        """Текущий синий канал, 0–255."""
        return 0


class _LedDriver:
    @staticmethod
    def on(
        r: int | ColorName,
        g: int = 0,
        b: int = 0,
        id: Index = "all",
        index: int = 1,
    ) -> None:
        """Цвет светодиода 1–96 или всех (``all``)."""

    @staticmethod
    def show(color: str, index: int = 1) -> None:
        """Цвета ленты строкой. Берутся первые 12 светодиодов."""

    @staticmethod
    def off(led_id: Index = "all", index: int = 1) -> None:
        """Погасить светодиод 1–96 или все."""

    @staticmethod
    def set_red(val: int, led_id: Index = "all", index: int = 1) -> None:
        """Красный канал, 0–255."""

    @staticmethod
    def set_green(val: int, led_id: Index = "all", index: int = 1) -> None:
        """Зелёный канал, 0–255."""

    @staticmethod
    def set_blue(val: int, led_id: Index = "all", index: int = 1) -> None:
        """Синий канал, 0–255."""

    @staticmethod
    def add_red(val: int, led_id: Index = "all", index: int = 1) -> None:
        """Прибавить красный, от -255 до 255."""

    @staticmethod
    def add_green(val: int, led_id: Index = "all", index: int = 1) -> None:
        """Прибавить зелёный, от -255 до 255."""

    @staticmethod
    def add_blue(val: int, led_id: Index = "all", index: int = 1) -> None:
        """Прибавить синий, от -255 до 255."""

    @staticmethod
    def set_mode(mode: Literal["steady", "breath", "marquee"] = "steady", index: int = 1) -> None:
        """Режим ленты: ``steady``, ``breath`` или ``marquee``."""


class _Speaker:
    @staticmethod
    def mute(index: int = 1) -> None:
        """Остановить динамик."""

    @staticmethod
    def play_tone(freq: int, index: int = 1) -> None:
        """Тон 20–5000 Гц. Выше 5000 Гц динамик играет 5000."""

    @staticmethod
    def play_music(music: str, index: int = 1) -> None:
        """Играть mp3 по имени файла, не дожидаясь конца."""

    @staticmethod
    def play_music_until_done(music: str, index: int = 1) -> None:
        """Играть mp3 и дождаться конца."""

    @staticmethod
    def set_vol(val: int, index: int = 1) -> None:
        """Громкость 0–100."""

    @staticmethod
    def add_vol(val: int, index: int = 1) -> None:
        """Изменить громкость на val, от -100 до 100."""

    @staticmethod
    def get_vol(index: int = 1) -> int:
        """Текущая громкость, 0–100."""
        return 0

    @staticmethod
    def is_play(index: int = 1) -> bool:
        """Динамик сейчас играет."""
        return False


class _MotorDriver:
    @staticmethod
    def set(power: float, index: int = 1) -> None:
        """Мощность мотора, от -100 до 100 процентов."""

    @staticmethod
    def add(power: float, index: int = 1) -> None:
        """Прибавить мощность, от -200 до 200 процентов."""

    @staticmethod
    def get(index: int = 1) -> float:
        """Текущая мощность, от -100 до 100."""
        return 0.0

    @staticmethod
    def get_load(index: int = 1) -> int:
        """Нагрузка мотора, 0–1024. Большое значение — затор или короткое замыкание."""
        return 0

    @staticmethod
    def stop(index: int = 1) -> None:
        """Остановить мотор."""


class _ServoDriver:
    @staticmethod
    def set(angle: float, index: int = 1) -> None:
        """Угол сервопривода, 0–180."""

    @staticmethod
    def add(angle: float, index: int = 1) -> None:
        """Сдвинуть сервопривод на angle градусов, от -180 до 180."""

    @staticmethod
    def get(index: int = 1) -> float:
        """Последний заданный угол, 0–180."""
        return 0.0

    @staticmethod
    def get_load(index: int = 1) -> int:
        """Нагрузка сервопривода, 0–1024."""
        return 0

    @staticmethod
    def release(index: int = 1) -> None:
        """Отпустить сервопривод. После этого get() уже не показывает реальный угол."""


class _SmartServo:
    @staticmethod
    def turn(angle: float, speed: float, index: int = 1) -> None:
        """Повернуть на angle от текущего положения. Плюс — по часовой. Ждёт конца."""

    @staticmethod
    def turn_to(angle: float, speed: float, index: int = 1) -> None:
        """Повернуть в угол angle. Ждёт конца."""

    @staticmethod
    def run(power: float, index: int = 1) -> None:
        """Крутить с мощностью 0–100."""

    @staticmethod
    def drive(power: float, t: float | Literal["forever"] = "forever", index: int = 1) -> None:
        """Крутить с мощностью power.

        В списке функций рядом описаны turn, turn_to и run. drive указан
        как команда, после которой отпущенный сервопривод снова удерживается.
        t по тексту — ``forever``.
        """

    @staticmethod
    def stop(index: Index = "all") -> None:
        """Остановить. index: номер или ``all``."""

    @staticmethod
    def get_angle(index: int = 1) -> float:
        """Угол от нулевой точки."""
        return 0.0

    @staticmethod
    def get_speed(index: int = 1) -> float:
        """Скорость, градусы в секунду."""
        return 0.0

    @staticmethod
    def release_angle(index: Index = "all") -> None:
        """Отпустить вал, чтобы его можно было повернуть рукой."""

    @staticmethod
    def lock_angle(index: Index = "all") -> None:
        """Удерживать текущий угол."""

    @staticmethod
    def reset(index: Index = "all") -> None:
        """Считать текущее положение нулём. Вызов занимает около трёх секунд."""


class _Ir:
    @staticmethod
    def send(message: str, index: int = 1) -> None:
        """Отправить ИК-сообщение, до 30 символов латиницы."""

    @staticmethod
    def receive(index: int = 1) -> str:
        """Последнее принятое ИК-сообщение."""
        return ""

    @staticmethod
    def record(record_id: int, index: int = 1) -> None:
        """Записать ИК-сигнал в слот 1 или 2. Вызов занимает около трёх секунд."""


button = _Button()
angle_sensor = _AngleSensor()
slider = _Slider()
joystick = _Joystick()
multi_touch = _MultiTouch()
science = _Science()
quad_rgb_sensor = _QuadRgb()
ultrasonic2 = _Ultrasonic2()
light_sensor = _LightSensor()
dual_rgb_sensor = _DualRgb()
sound_sensor = _SoundSensor()
pir = _Pir()
ultrasonic = _Ultrasonic()
ranging_sensor = _RangingSensor()
motion_sensor = _MotionSensor()
soil_sensor = _SoilSensor()
temp_sensor = _TempSensor()
humiture = _Humiture()
mq2 = _Mq2()
flame_sensor = _FlameSensor()
magnetic_sensor = _MagneticSensor()
smart_camera = _SmartCamera()
led_matrix = _LedMatrix()
rgb_led = _RgbLed()
led_driver = _LedDriver()
speaker = _Speaker()
motor_driver = _MotorDriver()
servo_driver = _ServoDriver()
smart_servo = _SmartServo()
ir = _Ir()

__all__ = [
    "button",
    "angle_sensor",
    "slider",
    "joystick",
    "multi_touch",
    "science",
    "quad_rgb_sensor",
    "ultrasonic2",
    "light_sensor",
    "dual_rgb_sensor",
    "sound_sensor",
    "pir",
    "ultrasonic",
    "ranging_sensor",
    "motion_sensor",
    "soil_sensor",
    "temp_sensor",
    "humiture",
    "mq2",
    "flame_sensor",
    "magnetic_sensor",
    "smart_camera",
    "led_matrix",
    "rgb_led",
    "led_driver",
    "speaker",
    "motor_driver",
    "servo_driver",
    "smart_servo",
    "ir",
]
