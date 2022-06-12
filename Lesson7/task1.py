class Matrix:
    def __init__(self, data):
        self.data = data
        for line in self.data[:-1]:
            if not len(line) == len(self.data[self.data.index(line) + 1]):
                raise ValueError('Размерность матриц не совпадает')

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in line) for line in self.data)

    def __add__(self, other):
        for i in range(len(self.data)):
            if not len(self.data[i]) == len(other.data[i]):
                raise ValueError('Размерность матриц не совпадает')
        item = [[int(self.data[line][num]) + int(other.data[line][num]) for num in range(len(self.data[line]))] for line
                in range(len(self.data))]
        return Matrix(item)
m1 = [[1, 2, 3], [4,5,6]]
m2=[[1,3,5],[2,4,6]]
matrix1=Matrix(m1)
matrix2=Matrix(m2)
print (matrix1)
print ('_____________________')
print (matrix2)
print ('_____________________')
print (matrix1+matrix2)