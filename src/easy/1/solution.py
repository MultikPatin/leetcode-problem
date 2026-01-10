from src.helper import tester

test_data = [
    {"args": ([2, 7, 11, 15], 9), "expected": [0, 1]},
    {"args": ([3, 2, 4], 6), "expected": [1, 2]},
    {"args": ([3, 3], 6), "expected": [0, 1]},
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
    tester(solution=Solution, task_name="twoSum", test_data=test_data)
