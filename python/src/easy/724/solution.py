from src.helper import Fields, tester

test_data = [
    {Fields.args: ([-1, -1, -1, -1, -1, 0],), Fields.expd: 2},
    {Fields.args: ([1, 7, 3, 6, 5, 6],), Fields.expd: 3},
    {Fields.args: ([1, 2, 3],), Fields.expd: -1},
    {Fields.args: ([2, 1, -1],), Fields.expd: 0},
]


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:  # noqa: N802
        left_sum, right_sum = 0, sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1

    # def pivotIndex(self, nums: list[int]) -> int:  # noqa: N802
    #     px = [0]
    #     for n in nums:
    #         px.append(px[-1] + n)
    #
    #     for i in range(1, len(px)):
    #         if px[-1] - px[i] == px[i - 1]:
    #             return i - 1
    #     return -1


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.pivotIndex, test_data=test_data)
