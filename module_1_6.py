my_dict = {
    'Danil': '23.10.2001',
    'Matvey': '02.06.2001',
    'Dima': '14.11.2001'}
print('Dict:', my_dict)

print('Existing value:', my_dict['Danil'])
print('Not existing value:', my_dict.get('Anton'))

my_dict.update({
    'Nikita': '31.05.2001',
    'Alena': '04.06.1999'})

deleted_value = my_dict.pop('Dima')
print('Deleted value:', deleted_value)

print('Modified dictionary:', my_dict)

my_set = {True, 'hello world', 15, 3.7, (1, 2, 3), True, 'hello world'}
print('\nSet:', my_set)
my_set.update([1337, False])
print('Modified set:', my_set)
