from src.helper import Fields, tester

test_data = [
    {Fields.args: ([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]],), Fields.expd: 16},
    {Fields.args: ([[1]],), Fields.expd: 4},
    {Fields.args: ([[1,0]],), Fields.expd: 4},
]


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:  # noqa: N802
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.islandPerimeter, test_data=test_data)
