from src.helper import Fields, tester

test_data = [
    {
        Fields.args: ([-100, -70, -60, 110, 120, 130, 160],),
        Fields.expd: [[-100, -60, 160], [-70, -60, 130]],
    },
    {
        Fields.args: ([-1, 0, 1, 2, -1, -4],),
        Fields.expd: [[-1, -1, 2], [-1, 0, 1]],
    },
    {Fields.args: ([0, 1, 1],), Fields.expd: []},
    {Fields.args: ([0, 0, 0],), Fields.expd: [[0, 0, 0]]},
]


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:  # noqa: N802
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return res

    # def threeSum(self, nums: list[int]) -> list[list[int]]:  # noqa: N802
    #     pos = defaultdict(list)
    #     for i, num in enumerate(nums):
    #         pos[num].append(i)
    #
    #     cache = set()
    #     triples = []
    #
    #     nums.sort()
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             target = 0 - nums[i] - nums[j]
    #             if target in cache:
    #                 idx_list = pos[target] + pos[nums[i]] + pos[nums[j]]
    #                 if len(set(idx_list)) >= 3:
    #                     triples.append((target, nums[i], nums[j]))
    #             cache.add(nums[i])
    #
    #     return [list(t) for t in set(triples)]


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.threeSum, test_data=test_data)
