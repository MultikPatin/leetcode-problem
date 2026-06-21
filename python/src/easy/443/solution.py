from src.helper import Fields, tester

test_data = [
    {Fields.args: (["a", "a", "a", "b", "b", "a", "a"],), Fields.expd: 6},
    # {Fields.args: (["a", "a", "b", "b", "c", "c", "c"],), Fields.expd: 6},
    # {Fields.args: (["a"],), Fields.expd: 1},
    # {
    #     Fields.args: (
    #         ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
    #     ),
    #     Fields.expd: 4,
    # },
]


class Solution:
    def compress(self, chars: list[str]) -> int:  # noqa: N802
        # cache = {}
        act_char = ""
        counter = 0
        # mask = []
        insert_idx = 0

        i = 0
        while i < len(chars):
            if chars[i] != act_char:
                chars[insert_idx] = chars[i]
                insert_idx += 1
                if counter != 1:
                    for c in str(counter):
                        chars[insert_idx] = c
                        insert_idx += 1
                counter = 1
                act_char = chars[i]
            else:
                counter += 1

            i += counter

        # mask.extend([act_char, counter])
        # mask = mask[2:]

        print(chars)

        # insert_idx = 0
        # i = 0
        # while i < len(chars):
        #     counter = cache[chars[i]]
        #     chars[insert_idx] = chars[i]
        #     insert_idx += 1
        #     if counter != 1:
        #         for c in str(counter):
        #             chars[insert_idx] = c
        #             insert_idx += 1
        #
        #     i += counter
        #
        # chars = chars[:insert_idx]
        return len(chars)


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.compress, test_data=test_data)
