import sys


def get_list_numbers() -> list[int]:
    return list(map(int, input().strip().split()))


def main():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        vertexs = get_list_numbers()
        for vertex in vertexs:
            matrix[i][vertex] = 1

    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
