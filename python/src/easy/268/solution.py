from src.helper import Fields, tester

test_data = [
    {Fields.args: ([3,0,1],), Fields.expd: 2},
    {Fields.args: ([0,1],), Fields.expd: 2},
    {Fields.args: ([9,6,4,2,3,5,7,0,1],), Fields.expd: 8},
]


class Solution:
    def missingNumber(self, nums: list[int]) -> int:  # noqa: N802
        m = len(nums)
        nums.sort()
        for i in range(m):
            if nums[i] != i:
                return i
        return m


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.missingNumber, test_data=test_data)
