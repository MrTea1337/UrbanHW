def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
#inner_function() Невозможно определить эту функцию, так как она вне пространства видимости и является локальной для test_function