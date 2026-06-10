from src.helper import Fields, tester

test_data = [
    {Fields.args: ([-4, -3, -2, 3, 3],), Fields.expd: [4, 9, 9, 9, 16]},
    {Fields.args: ([-2, 0],), Fields.expd: [0, 4]},
    {
        Fields.args: ([-10000, -9999, -7, -5, 0, 0, 10000],),
        Fields.expd: [0, 0, 25, 49, 99980001, 100000000, 100000000],
    },
    {Fields.args: ([-1],), Fields.expd: [1]},
    {Fields.args: ([-5, -3, -2, -1],), Fields.expd: [1, 4, 9, 25]},
    {Fields.args: ([-4, -1, 0, 3, 10],), Fields.expd: [0, 1, 9, 16, 100]},
    {Fields.args: ([-7, -3, 2, 3, 11],), Fields.expd: [4, 9, 9, 49, 121]},
]


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:  # noqa: N802
        neg = []

        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i] ** 2)
            else:
                right = i
                break
        else:
            return list(reversed(neg))

        res = []
        left = right

        while left < len(nums):
            p = nums[left] ** 2
            if right > 0:
                if p < neg[right - 1]:
                    res.append(p)
                    left += 1
                else:
                    res.append(neg[right - 1])
                    right -= 1
            else:
                res.append(p)
                left += 1

        if right > 0:
            res.extend(reversed(neg[:right]))

        return res


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.sortedSquares, test_data=test_data)
