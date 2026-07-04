import sys


def get_string_list() -> list[str]:
    return input().strip().split()


def main() -> None:
    n = int(input())
    counters = dict.fromkeys(get_string_list(), 0)
    m = int(input())

    if n - m > 1:
        print("NO")
        return

    for _ in range(m):
        v1, v2 = get_string_list()
        counters[v1] += 1
        counters[v2] += 1

    for v in counters.values():
        if v == 1:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main()
