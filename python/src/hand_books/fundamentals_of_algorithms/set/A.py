import sys


def get_list_numbers() -> list[int]:
    return list(map(int, input().strip().split()))


def main() -> None:
    n = int(input())
    s = set()
    res = []

    for _ in range(n):
        _type, num = get_list_numbers()
        if _type == 1:
            s.add(num)
        elif _type == 2:
            res.append(num in s)

    for r in res:
        print(int(r))


if __name__ == "__main__":
    main()
