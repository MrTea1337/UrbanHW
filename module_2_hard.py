import random


def too_old_ciper(n):
    password = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:                                        #Создание списка пар
                password += [i, j]

    str_password = ''
    for i in password:                                                  #Ковертация списка в строку
        str_password += str(i)
    return str_password


first_insert_list = random.sample(range(3, 21), 18)
for i in range(18):
    number_from_first_insert = first_insert_list[i]
    result = too_old_ciper(number_from_first_insert)
    print(f'Первый слот: {number_from_first_insert}\nПароль для решения: {result}')
