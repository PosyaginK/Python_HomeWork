########################################################################################################################
# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
########################################################################################################################
from abc import ABC, abstractmethod

class Clothers(ABC):

    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f'Создана новая вещь - {self.name}, Цвет - {self.color}')

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return f'На обе вещи понадобится {self.consumption + other.consumption} м.кв. ткани'

class Coat(Clothers):

    def __init__(self, name, color, size):
        self.size = size
        super().__init__(name, color)
        print(f'{self.name}: Размер - {self.size}\n{"-"*100}')

    @property
    def consumption(self):
        r = round(self.size / 6 + 0.5, 2)
        print(f'Чтобы изготовить {self.name} понадобится {r} м.кв. ткани')
        return r

class Suit(Clothers):

    def __init__(self, name, color, hight):
        self.hight = hight
        super().__init__(name, color)
        print(f'{self.name}: Рост - {self.hight} м\n{"-"*100}')

    @property
    def consumption(self):
        r = round(2 * self.hight + 0.3, 2)
        print(f'Чтобы изготовить {self.name} понадобится {r} м.кв. ткани')
        return r


c = Coat('Пальто', 'Черный', 52)
s = Suit('Костюм', 'Белый', 1.80)

print(c + s)