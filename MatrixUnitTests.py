import unittest
from matrix import Matrix


class MatrixTests(unittest.TestCase):
    def testIsValid(self):
        self.assertTrue(Matrix.is_valid([[1.9, 0],
                                         [2, 3.56]]))
        self.assertTrue(Matrix.is_valid([[1.5, 200, 40],
                                         [2, 3.7, 5]]))
        self.assertTrue(Matrix.is_valid([[complex(2, 3), 0.7],
                                         [2, complex(5, 0)]]))

        self.assertFalse(Matrix.is_valid([[1],
                                          [2, 3]]))
        self.assertFalse(Matrix.is_valid([]))
        self.assertFalse(Matrix.is_valid([["A", 0],
                                          [2, 3]]))

    def testAdd(self):
        A = Matrix([[5, 8], [9.5, 10]])
        B = Matrix([[6.57, 7], [complex(4, 7), 2]])
        C = Matrix([[11.57, 15], [complex(13.5, 7), 12]])

        self.assertEqual(C.Matrix, (A+B).Matrix)

    def testMultiply(self):
        A = Matrix([[-3, 4, -2], [1, 5, -4]])
        B = Matrix([[6, -1, 0], [7, 8, 3], [9, 1, 2]])
        C = Matrix([[-8, 33, 8], [5, 35, 7]])

        D = Matrix([[6, 7], [1, -1], [0, 2], [-2, -3]])
        E = Matrix([[3, 4, 5], [1, -1, 6]])
        F = Matrix([[25, 17, 72], [2, 5, -1], [2, -2, 12], [-9, -5, -28]])

        self.assertEqual(C.Matrix, (A * B).Matrix)
        self.assertEqual(F.Matrix, (D * E).Matrix)

    def testSubtract(self):
        A = Matrix([[5, 8], [9, 10]])
        B = Matrix([[6, 7], [3, 9]])
        C = Matrix([[-1, 1], [6, 1]])

        self.assertEqual(C.Matrix, (A - B).Matrix)

    def testScalair(self):
        A = Matrix([[5, 8], [9, 10]])
        c = 2

        B = Matrix([[10, 16], [18, 20]])

        self.assertEqual(B.Matrix, (A * c).Matrix)

    def testSlice(self):
        A = Matrix([[3, 4, 5], [4, 7, 9], [6, 9, 0]])
        A_sliced = Matrix([[4, 9], [6, 0]])

        self.assertEqual(A_sliced.Matrix, (Matrix.slice_matrix(A, 0, 1)).Matrix)

    def testDeterminant(self):
        A = Matrix([[3]])
        DetA = 3

        B = Matrix([[3, 5],
                    [7, 9]])
        DetB = -8

        C = Matrix([[1, -2, 3],
                    [2, 0, 3],
                    [1, 5, 4]])
        DetC = 25

        D = Matrix([[1, 2, 4],
                    [-1, 3, 0],
                    [4, 1, 0]])
        DetD = -52

        self.assertEqual(Matrix.determinant(A), DetA)
        self.assertEqual(Matrix.determinant(B), DetB)
        self.assertEqual(Matrix.determinant(C), DetC)
        self.assertEqual(Matrix.determinant(D), DetD)

    def testInverse(self):
        A = Matrix([[12, 3, -2],
                    [4, 9, -5],
                    [-6, -1, 4]])

        B = Matrix([[6, 8],
                    [2, 1]])

        C = Matrix([[7, -5, 23],
                    [7, 0, 2],
                    [-1, 3, 3]])

        D = Matrix([[5, 1, 3, 1],
                    [7, 8, -3, 0],
                    [4, 0, -5, 2],
                    [-2, 8, 9, 0]])

        self.assertEqual((A * (~A)).Matrix, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual((B * (~B)).Matrix, [[1, 0], [0, 1]])
        self.assertEqual((C * (~C)).Matrix, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual((D * (~D)).Matrix, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


if __name__ == '__main__':
    unittest.main()
