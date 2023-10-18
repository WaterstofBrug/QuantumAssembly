from matrix import Matrix


def main() -> None:
    print("hello world")
    matrix1 = Matrix([[0, 1, 4], [2, 0, 7], [-4, -6, 0]])
    matrix2 = Matrix([[0, 4], [3, 7]])
    ~matrix1


if __name__ == "__main__":
    main()
