from src.helper import Fields, tester

test_data = [
    {Fields.args: ([3,2,1],), Fields.expd: 1},
    {Fields.args: ([1,2],), Fields.expd: 2},
    {Fields.args: ([2,2,3,1],), Fields.expd: 1},
]


class Solution:
    def thirdMax(self, nums: list[int]) -> int:  # noqa: N802
        nums_set = list(set(nums))
        nums_set.sort()
        if len(nums_set) > 2:
            return nums_set[-3]
        return nums_set[-1]


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.thirdMax, test_data=test_data)
