from python.src.helper import Fields, tester

test_data = [
    {Fields.args: ("()",), Fields.expd: True},
    {Fields.args: ("()[]{}",), Fields.expd: True},
    {Fields.args: ("(]",), Fields.expd: False},
    {Fields.args: ("([])",), Fields.expd: True},
    {Fields.args: ("([)]",), Fields.expd: False},
]


class Solution:
    def isValid(self, s: str) -> bool:  # noqa: N802
        chars = []
        brackets = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in brackets:
                chars.append(c)
            elif len(chars) != 0 and brackets[chars[-1]] == c:
                chars.pop()
            else:
                chars.append(c)
                break

        return len(chars) == 0


if __name__ == "__main__":
    tester(solution=Solution, task_name="isValid", test_data=test_data)
