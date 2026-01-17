from python.src.helper import Fields, tester

test_data = [
    {Fields.args: (5,), Fields.expd: 5},
    {Fields.args: (5,), Fields.expd: 5},
    {Fields.args: (5,), Fields.expd: 5},
]


class Solution:
    def task(self, num: int) -> int:  # noqa: N802
        return num


if __name__ == "__main__":
    tester(solution=Solution, task_name="task", test_data=test_data)
