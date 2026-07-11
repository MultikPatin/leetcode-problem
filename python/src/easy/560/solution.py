from src.helper import Fields, tester

test_data = [
    {Fields.args: ([-1, -1, 1], 0), Fields.expd: 1},
    {Fields.args: ([1], 0), Fields.expd: 0},
    {Fields.args: ([1, 1, 1], 2), Fields.expd: 2},
    {Fields.args: ([1, 2, 3], 3), Fields.expd: 2},
]


# def get_prefix_sum(nums: list[int]) -> list[int]:
#     px = [0]
#     for n in nums:
#         px.append(px[-1] + n)
#     return px


class Solution:
    # def subarraySum(self, nums: list[int], k: int) -> int:  # noqa: N802
    #     px = {0: 1}
    #     curr_sum = 0
    #     count = 0
    #
    #     for num in nums:
    #         curr_sum += num
    #         count += px.get(curr_sum - k, 0)
    #         px[curr_sum] = px.get(curr_sum, 0) + 1
    #     return count

    def subarraySum(self, nums: list[int], k: int) -> int:  # noqa: N802
        px = {0: 1}
        count = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            sub = curr_sum - k
            if sub in px:
                count += px[sub]
            if curr_sum in px:
                px[curr_sum] += 1
            else:
                px[curr_sum] = 1

        return count


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.subarraySum, test_data=test_data)
