##################################################################################################################################
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо
# запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
##################################################################################################################################

num_list = [2, 5, 7, 3, 2]
new_el = None

print(f'Рейтинг - {sorted(num_list)[::-1]}')

while True:
    new_el = input('Введите новый элемент рейтинга: ')
    if new_el.isdigit():
        new_el = int(new_el)
        break
    else:
        continue
print(f'Новый элемент - {new_el}')

num_list.append(new_el)
num_list = sorted(num_list)
print(f'Обновленный рейтинг - {num_list[::-1]}')