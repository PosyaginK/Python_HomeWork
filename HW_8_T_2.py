########################################################################################################################
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.
########################################################################################################################

class NullDivision:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def div_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль запрещено")


div = NullDivision(10, 100)
print(NullDivision.div_null(10, 0))
print(NullDivision.div_null(10, 0.1))
print(div.div_null(100, 0))