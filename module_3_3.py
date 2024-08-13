def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1.Функция с параметрами по умолчанию:
print_params(b = 25)      #Выдаёт предупреждение, что ожидался другой тип данных
print_params(c = [1,2,3])

#2.Распаковка параметров:
values_list = ['string', False, 0]
values_dict = {'a': 7, 'b': False, 'c': [1, 2, 8]}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
