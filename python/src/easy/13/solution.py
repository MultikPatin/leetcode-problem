from python.src.helper import Fields, tester

test_data = [
    {Fields.args: ("III",), Fields.expd: 3},
    {Fields.args: ("LVIII",), Fields.expd: 58},
    {Fields.args: ("MCMXCIV",), Fields.expd: 1994},
]


class Solution:
    def romanToInt(self, s: str) -> int:  # noqa: N802
        trans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        n = len(s)
        for i in range(n):
            if i < n - 1 and trans[s[i]] < trans[s[i + 1]]:
                result -= trans[s[i]]
            else:
                result += trans[s[i]]
        return result


if __name__ == "__main__":
    tester(solution=Solution, task_name="romanToInt", test_data=test_data)
