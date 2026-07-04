import sys


def get_list_numbers() -> list[int]:
    return list(map(int, input().strip().split()))


def main() -> None:
    n = int(input())
    s: set[int] = set()

    for _ in range(n):
        row = get_list_numbers()
        s.update(row[1:])

    print(len(s))


if __name__ == "__main__":
    main()
