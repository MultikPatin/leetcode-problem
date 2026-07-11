from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1, 3, 4, 2, 2],), Fields.expd: 2},
    {Fields.args: ([3, 1, 3, 4, 2],), Fields.expd: 3},
    {Fields.args: ([3, 3, 3, 3, 3],), Fields.expd: 3},
]


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:  # noqa: N802
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.findDuplicate, test_data=test_data)
