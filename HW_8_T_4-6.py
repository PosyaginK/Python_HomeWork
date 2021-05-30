########################################################################################################################
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
########################################################################################################################
########################################################################################################################
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
########################################################################################################################
########################################################################################################################
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.
########################################################################################################################

class Warehouse:

    big_list = []

    def __init__(self):
        print('Склад оргтехники!')


class OfficeEquipment:

    def __init__(self, model, price, count):
        self.model = model
        self.price = price
        self.count = int(count)

class Printers(OfficeEquipment):

    name = 'Принтер'

    def __init__(self, model, price, count, colores, speed, *args):
        super().__init__(model, price, count)
        self.colores = colores
        self.speed = speed
        self.self_dict = {}
        self.printer_dict = {'name': Printers.name, 'model': self.model, 'count': self.count}
        Warehouse.big_list.append(self.printer_dict)

    def __str__(self):
        return f"{Printers.name} с параметрами:\nМарка - {self.model},\nЦена - {self.price} (руб.),\nКоличество - {self.count} (шт.),\n\
Цвета - {self.colores},\nСкорость - {self.speed} (стр./мин.)\n{'-'*100}"

    def send_to_warehouse(self, *args):
        self.printer_dict = {'name': Printers.name, 'model': self.model, 'count': self.count}


class Scaners(OfficeEquipment):

    name = 'Сканер'

    def __init__(self, model, price, count, max_format, color_depth):
        super().__init__(model, price, count)
        self.max_format = max_format
        self.color_depth = color_depth
        self.scaner_dict = {'name': Scaners.name, 'model': self.model, 'count': self.count}
        Warehouse.big_list.append(self.scaner_dict)

    def __str__(self):
        return f"{Scaners.name} с параметрами:\nМарка - {self.model},\nЦена - {self.price} (руб.),\nКоличество - {self.count} (шт.),\n\
Максимальный формат - {self.max_format},\nГлубина цвета - {self.color_depth}\n{'-'*100}"

class Xeroxs(OfficeEquipment):

    name = 'Ксерокс'

    def __init__(self, model, price, count, os, papper):
        super().__init__(model, price, count)
        self.os = os
        self.papper = papper
        self.xerox_dict = {'name': Xeroxs.name, 'model': self.model, 'count': self.count}
        Warehouse.big_list.append(self.xerox_dict)

    def __str__(self):
        return f"{Xeroxs.name} с параметрами:\nМарка - {self.model},\nЦена - {self.price} (руб.),\nКоличество - {self.count} (шт.),\n\
Операционная система - {self.os},\nБумага - {self.papper}\n{'-'*100}"


printer1 = Printers('LG', 10000, 2, 'RGB', 100)
print(printer1)

printer2 = Printers('Cannon', 10000, 5, 'RGB', 100)

scaner1 = Scaners('HP', 12500, 7, 'A3', '16 млн. цветов')
print(scaner1)

xerox1 = Xeroxs('Sony', 6000, 3, 'Windows', 'Любая')
print(xerox1)
print('На складе сейчас:')
for i in Warehouse.big_list:
    print(i)