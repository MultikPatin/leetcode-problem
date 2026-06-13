from src.helper import Fields, tester

test_data = [
    {Fields.args: ("badc", "baba"), Fields.expd: False},
    {Fields.args: ("bbbaaaba", "aaabbbba"), Fields.expd: False},
    {Fields.args: ("egg", "add"), Fields.expd: True},
    {Fields.args: ("f11", "b23"), Fields.expd: False},
    {Fields.args: ("paper", "title"), Fields.expd: True},
]


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:  # noqa: N802
        s_to_t = {}
        t_to_s = {}

        for sc, tc in zip(s, t, strict=True):
            if sc in s_to_t and s_to_t[sc] != tc:
                return False
            if tc in t_to_s and t_to_s[tc] != sc:
                return False

            s_to_t[sc] = tc
            t_to_s[tc] = sc

        return True


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.isIsomorphic, test_data=test_data)
