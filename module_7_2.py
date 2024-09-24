def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf8')
    i = 0
    strings_positions = {}
    for string in strings:
        i += 1
        strings_positions[(i, file.tell())] = string
        file.write(f'{string}\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
