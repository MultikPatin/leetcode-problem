from src.helper import Fields, tester

test_data = [
    {Fields.args: ([0, 1, 0, 3, 12],), Fields.expd: [1, 3, 12, 0, 0]},
    {Fields.args: ([0],), Fields.expd: [0]},
]


class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:  # noqa: N802
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1

        return nums


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.moveZeroes, test_data=test_data)
