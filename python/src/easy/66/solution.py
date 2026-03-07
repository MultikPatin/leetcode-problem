from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1,2,3],), Fields.expd: [1,2,4]},
    {Fields.args: ([4,3,2,1],), Fields.expd: [4,3,2,2]},
    {Fields.args: ([9],), Fields.expd: [1,0]},
]


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:  # noqa: N802
        res = 1
        for i, num in enumerate(reversed(digits)):
            res += num * 10 ** i
        return [int(x) for x in str(res)]


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.plusOne, test_data=test_data)
