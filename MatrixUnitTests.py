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


if __name__ == '__main__':
    unittest.main()
