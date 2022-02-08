import numpy as np
from random import randrange


class Matrix:
    def __init__(self, arr=None, shape=None, one=False):

        if arr is None:

            if one:
                self.arr = np.zeros(shape, int)
                np.fill_diagonal(self.arr, 1)
                return

            arr = []
            for i in range(shape[0]):
                arr.append([])
                for j in range(shape[1]):
                    arr[-1].append(randrange(0, 40))

        self.arr = np.array(arr)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.arr.dot(other.arr))
        return Matrix((self.arr * other).tolist())

    def __pow__(self, s):
        return Matrix(np.linalg.matrix_power(self.arr, s))

    def inv(self):
        return self ** -1

    def T(self):
        return Matrix(self.arr.T.tolist())

    def __invert__(self):
        return self.T()

    def __str__(self):
        return 'Matrix\n' + '\n'.join([' '.join(map(str, i)) for i in self.arr])

    def shape(self):
        return len(self.arr), len(self.arr[0])

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.arr.tolist()[key]
        return self.arr[key[0]][key[1]]

    def __setitem__(self, key, value):
        if isinstance(key, int):
            pass  # Лень писать
        self.arr[key[0]][key[1]] = value

    def __add__(self, other):
        m = Matrix(shape=self.shape())
        if isinstance(other, Matrix):
            for i in range(self.shape()[0]):
                for j in range(self.shape()[1]):
                    m[i, j] = self[i, j] + other[i, j]
            return m

    def det(self):
        return np.linalg.det(self.arr)


if __name__ == '__main__':
    m1 = Matrix(shape=(2, 3))
    m2 = Matrix(shape=(3, 3))
    m3 = Matrix(shape=(3, 3))

    print(m1 * m2)





