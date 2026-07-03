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


def main():
    matrix = get_matrix_numbers()
    for row in matrix:
        idxs = [i for i, x in enumerate(row) if x == 1]
        print(*idxs)


if __name__ == "__main__":
    main()
