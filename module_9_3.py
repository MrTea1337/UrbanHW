

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(pair[0]) - len(pair[1])) for pair in zip(first, second) if pair[0] != pair[1])
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))
