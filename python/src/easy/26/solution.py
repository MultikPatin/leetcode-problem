from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1,1,2],), Fields.expd: 2},
    {Fields.args: ([0,0,1,1,1,2,2,3,3,4],), Fields.expd: 5},
]


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:  # noqa: N802
        count = 0
        last = 111
        for num in nums:
            if num != last:
                nums[count] = num
                count += 1
                last = num
        return count


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.removeDuplicates, test_data=test_data)
