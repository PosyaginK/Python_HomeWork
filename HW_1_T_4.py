########################################################################################################################
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции.
########################################################################################################################

i = int()
while i <= 0:
    i = int(input('Введите целое положительное число: '))
print('Вы ввели число', i)
num = i

f = i%10
while i >= 1:
    i = i//10
    if i%10 > f:
        f = i%10
    if i > 9:
        continue
    else:
        print('Самая большая цифра в числе {} - {}' .format(num, f))
        break