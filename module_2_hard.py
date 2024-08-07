def too_old_ciper(n):
    password = []
    for i in range(1, n):
        for j in range(1, n):
            if n % (i + j) == 0 and i != j:                             #Создание списка пар
                password += [i, j]
                for k in range(0, len(password) - 1):
                    if password[k] == j and password[k + 1] == i:       #Удаление дублей пар
                        del password[len(password) - 2: len(password)]
                        break
    str_password = ''
    for i in password:                                                  #Ковертация списка в строку
        str_password += str(i)
    return str_password


number_from_first_insert = int(input('Введите число из первой вставки: '))
result = too_old_ciper(number_from_first_insert)
print(f'Пароль для решения : {result}')
