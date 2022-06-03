my_list = [56, "aff", True, [10, 12]]
print(type(my_list))
for i, item in enumerate(my_list):
    print (f"Переменная {item} c индексом {i} имеет тип {type(item)}")
