import sys


def get_list_numbers() -> list[int]:
    return list(map(int, input().strip().split()))


def get_matrix_numbers(n: int) -> list[list[int]]:
    matrix = []

    for _ in range(n):
        row = get_list_numbers()
        matrix.append(row)
    return matrix


def main():
    count = 0
    n = int(input())
    matrix = get_matrix_numbers(n)
    for i in range(n):
        links = [x for x in matrix[i] if x != 0]
        if len(links) == 1:
            count += 1
            print(i)

    if count == 0:
        print("NO LEAVES")


if __name__ == "__main__":
    main()
