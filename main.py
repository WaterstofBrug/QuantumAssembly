from matrix import Matrix


def main() -> None:
    print("hello world")
    matrix1 = Matrix([[0, 1], [2, 0]])
    matrix2 = Matrix([[0, 4], [3, 7]])
    print(matrix1.Matrix)
    print(matrix2.Matrix)
    print((matrix1 + matrix2))


if __name__ == "__main__":
    main()
