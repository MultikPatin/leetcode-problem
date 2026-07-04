import sys


def get_string_set() -> set[str]:
    return set(input().strip().split())


def get_edge_data() -> tuple[str, int, set[str]]:
    _in = input().strip().split()
    return _in[0], int(_in[1]), set(_in[2:])


def main():
    vg1 = get_string_set()
    vg2 = get_string_set()

    for _ in range(len(vg1)):
        edge = get_edge_data()
        if len(edge[2]) != len(vg2):
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()
