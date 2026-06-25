from collections import defaultdict

from src.helper import Fields, tester

test_data = [
    {Fields.args: ("ab", "a"), Fields.expd: False},
    {Fields.args: ("anagram", "nagaram"), Fields.expd: True},
    {Fields.args: ("rat", "car"), Fields.expd: False},
]


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  # noqa: N802
        if len(s) != len(t):
            return False

        s_spec = defaultdict(int)

        for char in s:
            s_spec[char] += 1

        for char in t:
            if char not in s_spec or s_spec[char] == 0:
                return False
            s_spec[char] -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.isAnagram, test_data=test_data)
