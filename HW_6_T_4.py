########################################################################################################################
# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
########################################################################################################################

class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.name = name
        self.is_police = is_police
        print(f'Создана машина {self.name}, цвет - {self.color}, максимальная скорость - {self.speed}')


    # Методы класса:
    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direcion):
       print(f'Машина {self.name} повернула {"налево" if direcion == 0 else "направо"}')

    def shpw_speed(self):
       print(f'Скорость автомобиля {self.name} - {self.speed}')
#
class TownCar(Car):

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}. Превышение скороси!'\
            if self.speed > 60 else f'Скорость автомобиля {self.name} - {self.speed}'

class SportCar(Car):

    def acceleration(self):
        return f'Машина ускорилась, теперь ее скорость составляет {self.speed + 10}'

class WorkCar(Car):

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}. Превышение скороси!'\
            if self.speed > 40 else f'Скорость автомобиля {self.name} - {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

zaz = WorkCar(100, 'Белый', 'Запорожец')
zaz.go()
zaz.turn(0)
zaz.turn(1)
zaz.stop()
input()
vol = TownCar(80, 'Черный', 'Вольво')
vol.go()
vol.turn(0)
vol.turn(1)
vol.stop()
print(vol.show_speed())
input()
fer = SportCar(320, 'Красный', 'Феррари')
fer.go()
fer.turn(0)
fer.turn(1)
fer.stop()
print(fer.acceleration())
input()
dps = PoliceCar(120, 'Бело-синий', 'ДПС')
dps.go()
dps.turn(0)
dps.turn(1)
dps.stop()
print(dps.is_police)
