##################################################################################################################################
# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input().
##################################################################################################################################
li = []
el = 1
count = int(input('Введите желаемое количество элементов списка: '))

while el <= count:
    val = input(f'Введите элемент {el} - ')
    li.append(val)
    el += 1

print(f'Исходный список - {li}')

i, j = 0, 1
while j < len(li):
    li[i], li[j] = li[j], li[i]
    i += 2
    j += 2
print(f'Измененнный список - {li}')
