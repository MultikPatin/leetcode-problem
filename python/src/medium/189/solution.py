from src.helper import Fields, tester

test_data = [
    {Fields.args: ([1, 2], 7), Fields.expd: [2, 1]},
    {
        Fields.args: ([1, 2, 3, 4, 5, 6, 7], 3),
        Fields.expd: [5, 6, 7, 1, 2, 3, 4],
    },
    {Fields.args: ([-1, -100, 3, 99], 2), Fields.expd: [3, 99, -1, -100]},
]


def rotate_sub_array(arr: list[int], i: int, j: int) -> None:
    j -= 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        length = len(nums)
        if k > length:
            k = k % length

        rotate_sub_array(nums, 0, len(nums))
        rotate_sub_array(nums, 0, k)
        rotate_sub_array(nums, k, len(nums))


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.rotate, test_data=test_data)
