from src.helper import Fields, tester

test_data = [
    {Fields.args: ([2, 2, 1],), Fields.expd: 1},
    {Fields.args: ([4, 1, 2, 1, 2],), Fields.expd: 4},
]


class Solution:
    def singleNumber(self, nums: list[int]) -> int:  # noqa: N802
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]
        return nums[-1]


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.singleNumber, test_data=test_data)
