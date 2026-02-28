from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1, 2, 3, 1], 3), Fields.expd: True},
    {Fields.args: ([1, 0, 1, 1], 1), Fields.expd: True},
    {Fields.args: ([1, 2, 3, 1, 2, 3], 2), Fields.expd: False},
]


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:  # noqa: N802
        last = {}
        for i, num in enumerate(nums):
            if num in last and abs(i - last[num]) <= k:
                return True
            last[num] = i
        return False


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.containsNearbyDuplicate, test_data=test_data)
