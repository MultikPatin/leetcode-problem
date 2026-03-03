from src.helper import Fields, tester

test_data = [
    {Fields.args: ([4, 3, 2, 7, 8, 2, 3, 1],), Fields.expd: [5, 6]},
    {Fields.args: ([1, 1],), Fields.expd: [2]},
]


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:  # noqa: N802
        all_nums = list(range(1, len(nums) + 1))
        return list(set(nums).symmetric_difference(all_nums))


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.findDisappearedNumbers, test_data=test_data)
