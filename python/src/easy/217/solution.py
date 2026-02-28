from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1, 2, 3, 1],), Fields.expd: True},
    {Fields.args: ([1, 2, 3, 4],), Fields.expd: False},
    {Fields.args: ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), Fields.expd: True},
]


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:  # noqa: N802
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.containsDuplicate, test_data=test_data)
