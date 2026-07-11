from src.helper import Fields, tester

test_data = [
    {
        Fields.args: ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1),
        Fields.expd: [[12, 21, 16], [27, 45, 33], [24, 39, 28]],
    },
    {
        Fields.args: ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2),
        Fields.expd: [[45, 45, 45], [45, 45, 45], [45, 45, 45]],
    },
]


def prefix_matrix(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    ps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            other = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]
            ps[i][j] = matrix[i - 1][j - 1] + other

    return ps


def sum_region(
    ps: list[list[int]], row1: int, col1: int, row2: int, col2: int
) -> int:
    row2 += 1
    col2 += 1
    return ps[row2][col2] - ps[row1][col2] - ps[row2][col1] + ps[row1][col1]


class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:  # noqa: N802
        ps = prefix_matrix(mat)
        n = len(mat)
        m = len(mat[0])

        res = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                s = sum_region(
                    ps,
                    max(i - k, 0),
                    max(j - k, 0),
                    min(i + k, n - 1),
                    min(j + k, m - 1),
                )
                res[i][j] = s
        return res


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.matrixBlockSum, test_data=test_data)
