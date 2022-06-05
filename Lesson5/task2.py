with open('file_1_1.txt', 'r', encoding='utf-8') as f:
    lines = 0
    words = 0
    for line in f:
        lines += 1
        for word in f:
            words = len(line.split())
        print('Количество слов:', words)
    print('Количество строк:', lines)
