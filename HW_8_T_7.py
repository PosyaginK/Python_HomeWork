########################################################################################################################
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
########################################################################################################################

class Complex:

    def __init__(self, real, img, *args):
        self.real = real
        self.img = img
        self.complex = f'{self.real} + {self.img}*i'

    def __add__(self, other):
        print(f'Сумма ({self.complex}) и ({other.complex}):')
        return f'***  {self.real + other.real} + {self.img + other.img}*i  ***'

    def __mul__(self, other):
        print(f'Произведение ({self.complex}) и ({other.complex}):')
        return f'***  {self.real * other.real - (self.img * other.img)} + {self.img + other.real}*i  ***'

    def __str__(self):
        return f'{self.real} + {self.img}*i'

num1 = Complex(1, -2)
num2 = Complex(3, 4)
print(f'Первое комплексное число: {num1}\nВторое комлпексное число: {num2}')
print('-'*100)
print(num1 + num2)
print('-'*100)
print(num1 * num2)
print('-'*100)