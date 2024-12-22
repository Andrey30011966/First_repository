def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, result):
            if result % i == 0:
                return f'Составное'
        return f'Простое'
    return wrapper

@is_prime
def sum_three(*args):
    result = sum(args)
    return result

result = sum_three(0, 0, 1)
print(result)