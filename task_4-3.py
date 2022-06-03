def my_func(x, y):
    try:
        x = float(x)
        y = int(y)

    except ValueError:
        print('Введите действительное число х и целое число у')
        return
    if x <= 0 or y >= 0:
        print('Введите положительное число х и отрицательное число у')
    return x ** y


print(my_func(input('Введите действительное полжительное число х: '), input('Введите целое отрицательное число у: ')))
