# Алгоритм Кнута-Морриса-Пратта используется
# для поиска подстроки (образца) в строке.
# O(n+m)
# Алгоритм Кнута-Морриса-Пратта используется
# для поиска подстроки (образца) в строке.
# O(n+m)
from python.src.helper import Fields, tester

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


class Solution:
    def search_index(self, data: str, sub: str) -> int:  # noqa: N802
        if data == "" or sub == "":
            return -1

        n = len(data)
        m = len(sub)
        p = [0] * m
        j = 0
        i = 1

        # Составляем массив смещений на основание префиксов и суффиксов
        while i < m:
            if sub[i] == sub[j]:
                p[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = p[j - 1]

        j = 0
        i = 0

        while i < n:
            if data[i] == sub[j]:
                i += 1
                j += 1
                if j == m:
                    return i - m
            elif j > 0:
                j = p[j - 1]
            else:
                i += 1

        return -1


if __name__ == "__main__":
    tester(solution=Solution, task_name="search_index", test_data=test_data)
