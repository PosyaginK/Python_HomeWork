########################################################################################################################
# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён после
# нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
########################################################################################################################

def my_sum(nums):
    num_list = []
    nums_sum = nums.split()
    if nums_sum[-1] == 'Q':
        nums_sum.pop(-1)
    for i in nums_sum:
        i = float(i)
        num_list.append(i)
    nums_sum = sum(num_list)
    return nums_sum

summ = float(0)
while True:
    nums = input('Для выхода нажмите Q\n Введите числа: ')
    if nums[-1] == 'Q':
        summ = my_sum(nums) + summ
        print(summ)
        break
    # my_sum(nums)
    summ = my_sum(nums) + summ
    print(summ)

print('Программа завершила работу')