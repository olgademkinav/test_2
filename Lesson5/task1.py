with open('file_1_1.txt', 'w', encoding='utf-8') as f:
    line = input('Введите текст: ')
    f.write(line + '\n')
    print(line, file=f)
