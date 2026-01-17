from python.src.helper import Fields, tester

test_data = [
    {Fields.args: ([7, 1, 5, 3, 6, 4],), Fields.expd: 5},
    {Fields.args: ([7, 6, 4, 3, 1],), Fields.expd: 0},
]


class Solution:
    def maxProfit(self, prices: list[int]) -> int:  # noqa: N802
        profit = 0
        last = prices[0]
        for price in prices[1:]:
            diff = last - price
            if diff > 0:
                last = price
            elif diff < profit:
                profit = last - price
        return abs(profit)


if __name__ == "__main__":
    tester(solution=Solution, task_name="maxProfit", test_data=test_data)
