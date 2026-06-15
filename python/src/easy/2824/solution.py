from src.helper import Fields, tester

test_data = [
    {Fields.args: ([6, -1, 7, 4, 2, 3], 8), Fields.expd: 8},
    {Fields.args: ([-1, 1, 2, 3, 1], 2), Fields.expd: 3},
    {Fields.args: ([-6, 2, 5, -2, -7, -1, 3], -2), Fields.expd: 10},
]


class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:  # noqa: N802
        if len(nums) <= 1:
            return 0

        nums.sort()

        i, j, pairs = 0, 1, 0

        while i < j < len(nums):
            if nums[i] + nums[j] < target:
                pairs += 1
            if j < len(nums) - 1:
                j += 1
            else:
                i += 1
                j = i + 1

        return pairs

    # def countPairs(self, nums: list[int], target: int) -> int:  # noqa: N802
    #     nums.sort()
    #     i = 0
    #     j = len(nums) - 1
    #     c = 0
    #     while i <= j:
    #         if nums[i] + nums[j] >= target:
    #             j -= 1
    #         else:
    #             c += j - i
    #             i += 1
    #
    #     return c


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.countPairs, test_data=test_data)
