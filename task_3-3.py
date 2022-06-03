def my_func(a, b, c):
    if a >= c and b >= c:
        return int(a) + int(b)
    elif a >= b and c >= b:
        return int(a) + int(c)
    else:
        return int(b) + int(c)


print(my_func(input('a '), input('b '), input('c ')))
