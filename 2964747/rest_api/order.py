from dataclasses import dataclass
from typing import List


@dataclass
class Order:
    order_id: int
    weight: float
    region: int
    delivery_hours: List[str]
    added_time: float = 0
    done_time: float = 0

    def __post_init__(self):
        # проверка поля weight
        if 0.01 > self.weight or self.weight > 50:
            raise (ValueError, 'Некорректный вес заказа')
        # проверка поля delivery_hours
        for time in self.delivery_hours:
            if len(time) != 11:
                raise (ValueError, 'Некорректное время доставки (длина)')
            a, b, c, d = 0, 0, 0, 0
            try:
                a = int(time[:2])
                b = int(time[3:5])
                c = int(time[6:8])
                d = int(time[9:])
            except:
                raise (ValueError, 'Некорректное время доставки (формат времени - числа)')

            if time[2] != ':' or time[5] != '-' or time[8] != ':':
                raise (ValueError, 'Некорректное время доставки (формат времени - разделители)')

            if not (0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 23 and 0 <= d <= 59):
                raise (ValueError, 'Некорректное время доставки (промежуток)')
