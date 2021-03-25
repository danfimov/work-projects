from dataclasses import dataclass, field
from typing import List


@dataclass
class Courier:
    courier_id: int
    courier_type: str
    regions: List[int]
    working_hours: List[str]
    _orders: List[int] = field(default_factory=list)

    @property
    def orders(self):
        return self._orders

    @property
    def max_weight_coefficient(self):
        if self.courier_type == 'foot':
            return 2
        elif self.courier_type == 'bike':
            return 5
        return 9


    def __post_init__(self):
        # проверка поля courier_id - уже была перед созданием объекта класса

        # проверка поля courier_type
        if self.courier_type not in ('foot', 'bike', 'car'):
            raise (ValueError, 'Некорректный тип курьера')

        # проверка поля regions
        for region in self.regions:
            assert (type(region) == int)

        # проверка поля working_hours
        for time in self.working_hours:
            if len(time) != 11:
                raise (ValueError, 'Некорректное время работы (длина)')
            a, b, c, d = 0, 0, 0, 0
            try:
                a = int(time[:2])
                b = int(time[3:5])
                c = int(time[6:8])
                d = int(time[9:])
            except:
                raise (ValueError, 'Некорректное время работы (формат времени - числа)')

            if time[2] != ':' or time[5] != '-' or time[8] != ':':
                raise (ValueError, 'Некорректное время работы (формат времени - разделители)')

            if not (0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 23 and 0 <= d <= 59):
                raise (ValueError, 'Некорректное время работы (промежуток)')
