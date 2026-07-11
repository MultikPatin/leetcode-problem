from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1, 3, 5, 4, 2, 3, 4, 5],), Fields.expd: 4},
    {Fields.args: ([1, 3, 5, 7],), Fields.expd: 4},
    {Fields.args: ([1, 3, 5, 4, 7],), Fields.expd: 3},
    {Fields.args: ([2, 2, 2, 2, 2],), Fields.expd: 1},
]


class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:  # noqa: N802
        res = 0
        curr = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1

        return max(res, curr)


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.findLengthOfLCIS, test_data=test_data)
