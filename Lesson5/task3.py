with open('file_3.txt', 'w', encoding='utf-8') as f:
    f.write('Иванов ')
    f.write('23543.12\n')
    f.write('Петров ')
    f.write('13749.32\n')
    f.write('Сидоров ')
    f.write('16543.12\n')
    f.write('Соловьев ')
    f.write('23749.32\n')
    f.write('Якименко ')
    f.write('29543.12\n')
    f.write('Кукушкин ')
    f.write('12749.32\n')
    f.write('Звонарев ')
    f.write('22543.12\n')
    f.write('Медведев ')
    f.write('18749.32\n')
    f.write('Ожерельев ')
    f.write('33543.12\n')
    f.write('Пономарев ')
    f.write('43749.32\n')
f.close()
with open('file_3.txt', 'r', encoding='utf-8') as f:
    names = []
    sum_income = 0
    aver_income = 0
    num = 0
    for line in f:
        num = num + 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(name)
        sum_income += income
        aver_income = sum_income / num
    print(names)
print(aver_income)
