from src.helper import tester

test_data = [
    {"args": [5], "expected": 5},
    {"args": [5], "expected": 5},
    {"args": [5], "expected": 5},
]


class Solution:
    def task(self, num: int) -> int:  # noqa: N802
        return num


if __name__ == "__main__":
    tester(solution=Solution, task_name="task", test_data=test_data)
