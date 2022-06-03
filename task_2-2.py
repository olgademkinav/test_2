my_list = input("Введите значение:").split()
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        j = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = j
        i = i + 1
else:
    i = 0
    while i < len(my_list) - 1:
        j = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = j
        i = i + 2
print(my_list)