# Алгоритм Бойера-Мура-Хорспула

from src.helper import Fields, tester

test_data = [
    {
        Fields.args: (
            "алилиллиллулд9у-лилиллилилулдвцвв вхцвлиллилилулд",
            "лилиллилилулд",
        ),
        Fields.expd: 16,
    },
    {
        Fields.args: ("abcabcabc", "abc"),
        Fields.expd: 0,
    },
    {
        Fields.args: ("aaaaaa", "aa"),
        Fields.expd: 0,
    },
    {
        Fields.args: ("hello world", "world"),
        Fields.expd: 6,
    },
    {
        Fields.args: ("hello world", "lo"),
        Fields.expd: 3,
    },
    {
        Fields.args: ("abcdef", "def"),
        Fields.expd: 3,
    },
    {
        Fields.args: ("abcdef", "xyz"),
        Fields.expd: -1,
    },
    {
        Fields.args: ("a", "a"),
        Fields.expd: 0,
    },
    {
        Fields.args: ("a", "b"),
        Fields.expd: -1,
    },
    {
        Fields.args: ("", "a"),
        Fields.expd: -1,
    },
    {
        Fields.args: ("s", ""),
        Fields.expd: -1,
    },
    {
        Fields.args: ("abababab", "abab"),
        Fields.expd: 0,
    },
    {
        Fields.args: ("abracadabra", "abra"),
        Fields.expd: 0,
    },
    {
        Fields.args: ("mississippi", "issi"),
        Fields.expd: 1,
    },
    {
        Fields.args: ("aaaaaaaaab", "aaab"),
        Fields.expd: 6,
    },
    {
        Fields.args: ("xxyxxxyxxx", "xxy"),
        Fields.expd: 0,
    },
    {
        Fields.args: ("testtest", "test"),
        Fields.expd: 0,
    },
]

PLACEHOLDER = "*"


def calculate_offsets(sub: str) -> tuple[dict[str, int], int]:
    m = len(sub)
    p = {PLACEHOLDER: m}

    for i in range(m - 2, -1, -1):  # итерации с предпоследнего символа
        if sub[i] not in p:  # если символ еще не добавлен в таблицу
            p[sub[i]] = m - i - 1

    if sub[m - 1] not in p:  # отдельно формируем последний символ
        p[sub[m - 1]] = m

    return p, m


class Solution:
    def search_index(self, data: str, sub: str) -> int:  # noqa: N802
        if data == "" or sub == "":
            return -1

        offsets, sub_length = calculate_offsets(sub)
        n = len(data)

        if n < sub_length:
            return -1

        i = sub_length - 1  # счетчик проверяемого символа в строке

        while i < n:
            k = 0

            for j in range(sub_length - 1, -1, -1):
                if data[i - k] != sub[j]:
                    if j == sub_length - 1:
                        off = offsets[data[i]] if offsets.get(data[i]) else offsets[PLACEHOLDER]
                    else:
                        off = offsets[sub[j]]  # смещение, если не равен не последний символ образа

                    i += off  # смещение счетчика строки
                    break

                k += 1  # смещение для сравниваемого символа в строке

            if k == sub_length:
                return i - k + 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.search_index, test_data=test_data)
