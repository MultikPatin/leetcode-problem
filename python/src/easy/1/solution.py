from src.helper import Fields, tester

test_data = [
    {Fields.args: ([2, 7, 11, 15], 9), Fields.expd: [0, 1]},
    {Fields.args: ([3, 2, 4], 6), Fields.expd: [1, 2]},
    {Fields.args: ([3, 3], 6), Fields.expd: [0, 1]},
]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:  # noqa: N802
        cache = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in cache:
                return [cache[res], i]
            cache[nums[i]] = i

        return []


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.twoSum, test_data=test_data)
