import sys


def get_list_numbers() -> list[int]:
    return list(map(int, input().strip().split()))


def main() -> None:
    n = int(input())
    s: set[int] = set()

    for _ in range(n):
        row = get_list_numbers()
        if row[0] == 0:
            continue
        if not s:
            s.update(row[1:])
        else:
            s = s.intersection(row[1:])

    print(len(s))


if __name__ == "__main__":
    main()
