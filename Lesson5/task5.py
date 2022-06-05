with open('file_5.txt', 'w', encoding='utf-8') as f:
    f.write(f"{''.join([str(i) for i in range(1, 100)])}")
with open('file_5.txt', 'r', encoding='utf-8') as f:
    num = [int(i) for i in f.read().split()]
    print(sum(num))
