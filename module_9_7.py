def is_prime(func):
    def surrogate(*args):
        result = func(*args)
        prime = True
        for i in range(2, result):
            if result % i == 0:
                prime = False
                break
        if prime:
            print('Простое')
        else:
            print('Составное')
        return result
    return surrogate


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
