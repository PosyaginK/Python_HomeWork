########################################################################################################################
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
########################################################################################################################
class Date:

    date = '01-01-2000'
    day = 1
    month = 1
    year = 2000

    def __init__(self, date):
        Date.date = date

    @classmethod
    def first(cls):
        date_list = []
        date_split = cls.date.split('-')
        print(date_split)
        for i in date_split:
            date_list.append(int(i))
        Date.day, Date.month, Date.year = date_list[0], date_list[1], date_list[2]
        return f'число - {Date.day:02}\nмесяц - {Date.month:02}\nгод - {Date.year}\n'

    @staticmethod
    def second():
        error = 0
        if Date.day < 1 or Date.day > 31:
            print('Вы ввели некорректный день.')
            error += 1
        if Date.month < 1 or Date.month > 12:
            print('Вы ввели некорректный месяц.')
            error += 1
        if Date.year < 1 or Date.year > 2020:
            print('Вы ввели некорректный год.')
            error += 1
        if error == 0:
            return f"Отлично. Вы ввели дату: {Date.day}-{Date.month}-{Date.year}"
        else:
            return "Попруйте еще раз"

#classmethod
my_date = Date('18-10-2020')
print(Date.first())
print(my_date.first())

#staticmethod
print(Date.second())