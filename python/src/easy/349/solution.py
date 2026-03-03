from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1,2,2,1],[2,2]), Fields.expd: [2]},
    {Fields.args: ([4,9,5],[9,4,9,8,4]), Fields.expd: [9,4]},
]


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:  # noqa: N802
        return list(set(nums1).intersection(nums2))


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.intersection, test_data=test_data)
