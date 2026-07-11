import sys


def get_list_numbers() -> list[int]:
    return list(map(int, input().strip().split()))


def main() -> None:
    n = int(input())
    s = {}
    res = []

    for _ in range(n):
        data = get_list_numbers()
        if data[0] == 1:
            s[data[1]] = data[2]
        elif data[0] == 2:
            if data[1] in s:
                res.append(s[data[1]])
            else:
                res.append(-1)

    for r in res:
        print(int(r))


if __name__ == "__main__":
    main()
