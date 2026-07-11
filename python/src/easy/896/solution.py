from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1, 2, 2, 3],), Fields.expd: True},
    {Fields.args: ([6, 5, 4, 4],), Fields.expd: True},
    {Fields.args: ([1, 3, 2],), Fields.expd: False},
]


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:  # noqa: N802
        if len(nums) <= 1:
            return True

        is_inc = True
        is_dec = True

        for i in range(1, len(nums)):
            if not is_inc and not is_dec:
                return False

            if nums[i] < nums[i - 1]:
                is_inc = False
            if nums[i] > nums[i - 1]:
                is_dec = False

        return is_inc or is_dec


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.isMonotonic, test_data=test_data)
