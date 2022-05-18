numeral = 1238587
max = numeral % 10
while numeral > 0:
    numeral = numeral // 10
    if numeral % 10 > max:
        max = numeral % 10
    if numeral > 9:
        continue
    else:
        print ('Наибольшее число:', max)