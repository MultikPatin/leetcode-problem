from src.helper import Fields, tester

test_data = [
    {Fields.args: (["h", "e", "l", "l", "o"],), Fields.expd: ["o", "l", "l", "e", "h"]},
    {Fields.args: (["H", "a", "n", "n", "a", "h"],), Fields.expd: ["h", "a", "n", "n", "a", "H"]},
]


class Solution:
    def reverseString(self, s: list[str]) -> None:  # noqa: N802
        le = 0
        rt = len(s) - 1

        while le < rt:
            temp = s[le]
            s[le] = s[rt]
            s[rt] = temp
            le += 1
            rt -= 1


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.reverseString(), test_data=test_data)
