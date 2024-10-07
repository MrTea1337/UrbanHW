first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(name) for name in first_strings if len(name) >= 5]
second_result = [(name_1, name_2) for name_1 in first_strings for name_2 in second_strings if len(name_1) == len(name_2)]
third_result = {name: len(name) for name in first_strings + second_strings if len(name) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
