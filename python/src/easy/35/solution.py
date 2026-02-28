from python.src.helper import Fields, tester

test_data = [
    {Fields.args: ([1, 3, 5, 6], 5), Fields.expd: 2},
    {Fields.args: ([1, 2, 3, 5, 6], 2), Fields.expd: 1},
    {Fields.args: ([1, 2, 3, 5, 6, 7], 6), Fields.expd: 4},
    {Fields.args: ([1, 2, 3, 5, 6, 7, 8, 9, 10, 11], 10), Fields.expd: 8},
    {Fields.args: ([1, 2, 3, 5, 6, 7, 8, 9, 10, 11], 6), Fields.expd: 4},
    {Fields.args: ([1, 3, 5, 6], 4), Fields.expd: 2},
    {Fields.args: ([1, 3, 5, 7], 6), Fields.expd: 3},
    {Fields.args: ([1, 3, 5, 6], 7), Fields.expd: 4},
]


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:  # noqa: N802
        li = 0
        ri = len(nums) - 1

        while li <= ri:
            mid = (li + ri) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                li = mid + 1
            else:
                ri = mid - 1

        return li


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.searchInsert, test_data=test_data)
