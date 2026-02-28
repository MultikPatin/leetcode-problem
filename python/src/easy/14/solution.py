from src.helper import Fields, tester

test_data = [
    {Fields.args: (["flower", "flow", "flight"],), Fields.expd: "fl"},
    {Fields.args: (["dog", "racecar", "car"],), Fields.expd: ""},
    {Fields.args: (["a"],), Fields.expd: "a"},
    {Fields.args: (["a", "b"],), Fields.expd: ""},
]


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:  # noqa: N802
        if not strs:
            return ""

        for i, chars in enumerate(zip(*strs, strict=False)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs) if set(strs) != {""} else ""


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.longestCommonPrefix, test_data=test_data)
