from collections import Counter
from typing import List

from python.src.helper import Fields, tester

test_data = [
    {Fields.args: ([3, 2, 3],), Fields.expd: 3},
    {Fields.args: ([2, 2, 1, 1, 1, 2, 2],), Fields.expd: 2},
]


class Solution:
    def majorityElement(self, nums: list[int]) -> int:  # noqa: N802
        return Counter(nums).most_common(1)[0][0]


if __name__ == "__main__":
    tester(solution=Solution, task_name="majorityElement", test_data=test_data)
