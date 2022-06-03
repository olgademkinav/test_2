def num(a, b):
    try:
        return (int(a) / int(b))
    except ZeroDivisionError:
        print("Делить на 0 нельзя")


print(num(input("Введите число а: "), input("Введите число b: ")))
