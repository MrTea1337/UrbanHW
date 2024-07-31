immutable_var = True, 'hello world', 15, 3.7, (1, 2, 3)
print(immutable_var)
#immutable_var[0] = False       Ничего не выйдет, т.к. кортеж является неизменяем объектом
mutable_list = [True, 'hello world', 15, 3.7, (1, 2, 3)]
mutable_list[1] = 'good bye world'
print(mutable_list)
