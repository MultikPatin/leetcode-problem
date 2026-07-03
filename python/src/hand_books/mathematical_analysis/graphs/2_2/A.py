import sys


def get_list_numbers() -> list[int]:
    return list(map(int, input().strip().split()))


def get_matrix_numbers() -> list[list[int]]:
    row = get_list_numbers()
    matrix = [row]

    for _ in range(len(row) - 1):
        row = get_list_numbers()
        matrix.append(row)
    return matrix


def main() -> None:
    matrix = get_matrix_numbers()
    median = [i for i in range(len(matrix)) if matrix[i][i] == 1]
    if median:
        for i in median:
            print(i)
    else:
        print("NO LOOPS")


if __name__ == "__main__":
    main()
