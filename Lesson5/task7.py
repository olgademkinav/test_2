import json

with open('file_7.txt', 'w', encoding='utf-8') as f:
    f.write("Фирма1 ООО 10000 5000 \n")
    f.write("Фирма2 ЗАО 20000 8000 \n")
    f.write("Фирма3 ИП 5000 3000 \n")
    f.write("Фирма4 ООО 7000 1000 \n")
    f.write("Фирма5 ООО 8000 1500 \n")
f.close()
res = dict()
aver_profit = 0
num = 0
with open('file_7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, type, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit > 0:
            aver_profit = aver_profit + profit
            num = num + 1
        res[name] = profit
    aver_profit = profit / num
with open('json_7.json', 'w', encoding='utf-8') as f:
    json.dump([res, aver_profit], f, ensure_ascii=False, indent=4)