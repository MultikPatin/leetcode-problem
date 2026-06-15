from src.helper import Fields, tester

test_data = [
    {Fields.args: ([2, 7, 11, 15], 9), Fields.expd: [1, 2]},
    {Fields.args: ([2, 3, 4], 6), Fields.expd: [1, 3]},
    {Fields.args: ([-1, 0], -1), Fields.expd: [1, 2]},
]


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:  # noqa: N802
        i, j = 0, len(numbers) - 1

        while i < j:
            result = numbers[i] + numbers[j]

            if result == target:
                return [i + 1, j + 1]
            if result < target:
                i += 1
            elif result > target:
                j -= 1

        return [i + 1, j + 1]

    def twoSum(self, numbers: list[int], target: int) -> list[int]:  # noqa: N802
        compliment = {}
        for i in range(len(numbers)):
            result = target - numbers[i]
            if result in compliment:
                return [compliment[result] + 1, i + 1]
            compliment[numbers[i]] = i
        return []


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.twoSum, test_data=test_data)
