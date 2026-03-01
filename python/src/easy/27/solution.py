from src.helper import Fields, tester

test_data = [
    {Fields.args: ([3, 2, 2, 3],3), Fields.expd: 2},
    {Fields.args: ([0, 1, 2, 2, 3, 0, 4, 2],2), Fields.expd: 5},
]


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:  # noqa: N802
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.removeElement, test_data=test_data)
