def int_func(text):
    return text[0].upper() + text[1:].lower()


print(int_func(input('Введите текст: ')))
