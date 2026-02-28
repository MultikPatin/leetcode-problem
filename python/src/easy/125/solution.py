from src.helper import Fields, tester

test_data = [
    {Fields.args: ("A man, a plan, a canal: Panama",), Fields.expd: True},
    {Fields.args: ("race a car",), Fields.expd: False},
    {Fields.args: (" ",), Fields.expd: True},
]


class Solution:
    def isPalindrome(self, s: str) -> bool:  # noqa: N802
        chars = [c for c in s.lower() if c.isalnum()]
        return chars == chars[::-1]


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.isPalindrome, test_data=test_data)
