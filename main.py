import numpy as np
from random import randrange


class Matrix:
    def __init__(self, arr=None, shape=None):

        if arr is None:
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


if __name__ == '__main__':
    m1 = Matrix(shape=(3, 3))
    print((m1 * 3) ** -1)




