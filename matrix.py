import cmath
from typing import List, Union
from icecream import ic


# The Matrix class handles all basic matrix calculations and has support for complex numbers


class Matrix:
    def __init__(self, matrix: List[List[Union[int, float, complex]]]):
        if not self.is_valid(matrix):
            raise Exception(f"Error: Invalid Matrix {matrix}")

        self.__matrix = matrix
        self.__height = len(matrix)
        self.__width = len(matrix[0])

    def __repr__(self):
        return f"Matrix({self.Matrix}, {self.Height}, {self.Width})"

    def __add__(self, other):
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

    def __iadd__(self, other):
        res_matrix = self + other
        self.Matrix = res_matrix.Matrix

    def __mul__(self, other):
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

    def __imul__(self, other):
        res_matrix = self * other
        self.Matrix = res_matrix.Matrix

    def scalair_multiply(self, c: Union[int, float, complex]):
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

    def __isub__(self, other):
        res_matrix = self - other
        self.Matrix = res_matrix.Matrix

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
