class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(self, row_len):
        result = ['*' * row_len] * (self.num // row_len)
        if self.num % row_len:
            result.append('*' * (self.num // row_len))
            return '\n'.join(result)

    def __str__(self):
        return f"{self.num}"

    def __add__(self, other):
        print('Сумма ячеек равна: ')
        return Cell(self.num + other.num)

    def __sub__(self, other):
        print('Вычитание ячеек равно: ')
        return Cell(self.num - other.num)

    def __mul__(self, other):
        print('Умножение ячеек равно: ')
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        print('Деление ячеек равно: ')
        return Cell(self.num // other.num)


cell_1 = Cell(12)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(11))
print(cell_2.make_order(7))
