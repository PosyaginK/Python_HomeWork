############################################################################################################################################
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
############################################################################################################################################
# list
months = ['Зима', 'Весна', 'Лето', 'Осень']
month = input('Введите номер месяца: ')

while True:
    if month == '1' or month == '2' or month == '12':
        print('Время года -', months[0])
        break
    elif month == '3' or month == '4' or month == '5':
        print('Время года -', months[1])
        break
    elif month == '6' or month == '7' or month == '8':
        print('Время года -', months[2])
        break
    elif month == '9' or month == '10' or month == '11':
        print('Время года -', months[3])
        break
    else:
        month = input('Введенные данне - не корректны (ведите номер месяца от 1 до 12)!!! - ')


# dict

months = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

while True:
    month = input('Введите номер месяца: ')
    if month.isdigit():
        month = int(month)
    else:
        continue
    if month in months['Зима']:
        print('Время года - Зима')
        break
    elif month in months['Весна']:
        print('Время года - Весна')
        break
    elif month in months['Лето']:
        print('Время года - Лето')
        break
    elif month in months['Осень']:
        print('Время года - Осень')
        break
    else:
        continue
