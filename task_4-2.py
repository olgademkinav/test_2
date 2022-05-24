test = input('Введите фразу ').split()
for i, word in enumerate(test,1):
    if len(word)<=10:
        print(i, word)
    else:
        print (i, word [:10])