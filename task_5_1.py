revenue = input ('Введите значение выручки')
costs = input ('Введите сумму издержек')
profit = int(revenue) - int(costs)
if profit > 0:
    profitability = profit / int(revenue) * 100
    print ('Прибыль равна:', profit)
    print ('Рентабельность составляет', profitability, '%')
else:
    print ('Убыток составляет:', profit)
number_of_employees = input ('Введите количество сотрудников')
if profit > 0:
    profitab_of_emp = profit / int(number_of_employees) * 100
    print ('Прибыль на одного работника составляет', profitab_of_emp, '%')
else:
    print('В Вашей фирме убыток')