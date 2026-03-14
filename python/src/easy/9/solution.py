from src.helper import Fields, tester

test_data = [
    {Fields.args: (121,), Fields.expd: True},
    {Fields.args: (-121,), Fields.expd: False},
    {Fields.args: (10,), Fields.expd: False},
]


class Solution:
    def isPalindrome(self, x: int) -> bool:  # noqa: N802
        if x <= 10:
            return False
        numbers = [num for num in str(x)]
        r = 0
        l = len(numbers) - 1
        while l > r:
            if numbers[r] == numbers[l]:
                r += 1
                l -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.isPalindrome, test_data=test_data)
