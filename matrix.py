from typing import List, Union, Type
from icecream import ic


# The Matrix class handles all basic matrix calculations and has support for complex numbers


class Matrix:
    def __init__(self, matrix: List[List[Union[int, float, complex]]]):
        if not self.is_valid(matrix):
            raise Exception(f"Error: Invalid Matrix {matrix}")

        self.__matrix = matrix
        self.__height = len(matrix)
        self.__width = len(matrix[0])

    def __repr__(self) -> str:
        return f"Matrix({self.Matrix}, {self.Height}, {self.Width})"

    def __add__(self, other: 'Matrix') -> 'Matrix':
        # check if addition is possible
        if type(self) != type(other):
            raise Exception(f"Error: Invalid operation on types {type(self)} and {type(other)}.")

        if self.Height != other.Height or \
                self.Width != other.Width:
            raise Exception(f"Error: Invalid operation ADDITION on {self} and {other}.")

        # handling addition
        new_matrix = self.Matrix.copy()

        for row in range(self.Height):
            for col in range(self.Width):
                new_matrix[row][col] += other.Matrix[row][col]

        return Matrix(new_matrix)

    def __iadd__(self, other: 'Matrix') -> None:
        res_matrix = self + other
        self.Matrix = res_matrix.Matrix

    def __mul__(self, other: Union['Matrix', int, float, complex]) -> 'Matrix':
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return self.scalair_multiply(other)

        # check if multiplication is possible
        if type(self) != type(other):
            raise Exception(f"Error: Invalid operation on types {type(self)} and {type(other)}.")

        if self.Width != other.Height:
            raise Exception(f"Error: Invalid operation MULTIPLICATION on {self} and {other}.")

        matrix = []
        for row in range(self.Height):
            matrix.append([])
            for col in range(other.Width):
                matrix[row].append(0)

                for i in range(other.Height):
                    matrix[row][col] += self.Matrix[row][i] * other.Matrix[i][col]

        return Matrix(matrix)

    def __imul__(self, other: Union['Matrix', int, float, complex]) -> None:
        res_matrix = self * other
        self.Matrix = res_matrix.Matrix

    def __invert__(self) -> 'Matrix':
        # note this is not a bitwise invert. This returns the inverse
        if not Matrix.is_square(self):
            raise Exception("Error: matrix not square")
        if not Matrix.determinant(self):
            raise Exception("Error> invertible matrix")

        matrix = self.Matrix.copy()

        inverse = [[int(i == j) for j in range(self.Width)] for i in range(self.Height)]

        for i, row in enumerate(matrix):
            factor = 1 / row[i]
            matrix[i] = [factor * elem for elem in matrix[i]]
            inverse[i] = [factor * elem for elem in inverse[i]]

            for j in range(self.Height):
                if j != i:
                    factor = matrix[j][i]
                    matrix[j] = [elem - factor * matrix[i][k] for k, elem in enumerate(matrix[j])]
                    inverse[j] = [elem - factor * inverse[i][k] for k, elem in enumerate(inverse[j])]

        return Matrix(inverse)

    def scalair_multiply(self, c: Union[int, float, complex]) -> 'Matrix':
        res_matrix = Matrix(self.Matrix.copy())

        for row in range(res_matrix.Height):
            for col in range(res_matrix.Width):
                res_matrix.Matrix[row][col] *= c

        return res_matrix

    def __sub__(self, other):
        # check if addition is possible
        if type(self) != type(other):
            raise Exception(f"Error: Invalid operation on types {type(self)} and {type(other)}.")

        if self.Height != other.Height or \
                self.Width != other.Width:
            raise Exception(f"Error: Invalid operation SUBTRACTION on {self} and {other}.")

        # cheeky subtract
        return self + other.scalair_multiply(-1)

    def __isub__(self, other: 'Matrix') -> None:
        res_matrix = self - other
        self.Matrix = res_matrix.Matrix

    def __round__(self, n: int = None) -> 'Matrix':
        matrix = self.Matrix.copy()
        for row in range(self.Width):
            for col in range(self.Height):
                matrix[row][col] = round(matrix[row][col], n)

        return Matrix(matrix)

    @property
    def Matrix(self) -> List[List[Union[int, float, complex]]]:
        return self.__matrix

    @property
    def Height(self) -> int:
        return self.__height

    @property
    def Width(self) -> int:
        return self.__width

    @Matrix.setter
    def Matrix(self, matrix: List[List[Union[int, float, complex]]]) -> None:
        if not self.is_valid(matrix):
            raise Exception(f"Error: Matrix too small.")
        self.__matrix = matrix
        self.__height = len(matrix)
        self.__width = len(matrix[0])

    @staticmethod
    def determinant(matrix: 'Matrix') -> Union[int, float, complex]:
        if not isinstance(matrix, Matrix) or not Matrix.is_square(matrix):
            raise Exception("Error: not valid object for Determinant")

        if matrix.Width == 1:
            return matrix.Matrix[0][0]
        elif matrix.Width == 2:
            return matrix.Matrix[0][0] * matrix.Matrix[1][1] - matrix.Matrix[0][1] * matrix.Matrix[1][0]
        else:
            return sum([(-1) ** i * matrix.Matrix[0][i] * Matrix.determinant(Matrix.slice_matrix(matrix, 0, i)) for i in
                        range(matrix.Width)])

    @staticmethod
    def slice_matrix(matrix: 'Matrix', row: int, col: int) -> 'Matrix':
        sliced_matrix = matrix.Matrix.copy()
        sliced_matrix = sliced_matrix[0:row] + sliced_matrix[row + 1:]

        for i, row in enumerate(sliced_matrix):
            sliced_matrix[i] = row[0:col] + row[col + 1:]

        return Matrix(sliced_matrix)

    @staticmethod
    def is_square(matrix: 'Matrix') -> bool:
        if not isinstance(matrix, Matrix):
            raise Exception("Error: type error must call is_square on Matrix.")

        return matrix.Height == matrix.Width

    @staticmethod
    def is_valid(matrix: List[List[Union[int, float, complex]]]) -> bool:
        if len(matrix) == 0:
            return False

        row_length = len(matrix[0])

        for row in matrix:
            if row_length != len(row):
                return False

            for elem in row:
                if not (isinstance(elem, int) or
                        isinstance(elem, float) or
                        isinstance(elem, complex)):
                    return False

        return True
