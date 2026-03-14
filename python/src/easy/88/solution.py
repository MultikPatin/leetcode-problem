from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3,), Fields.expd: [1, 2, 2, 3, 5, 6]},
    {Fields.args: ([1], 1, [], 0,), Fields.expd: [1]},
    {Fields.args: ([0], 0, [1], 1), Fields.expd: [1]},
]


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:  # noqa: N802
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.merge, test_data=test_data)
