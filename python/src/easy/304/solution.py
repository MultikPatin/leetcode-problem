class NumMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        # Создаём матрицу из 0 с размером на 1 больше по вертикали и горизонтали
        ps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        #  Заполняем префиксную матрицу
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Сумма всех элементов кроме текущего
                other = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]
                ps[i][j] = matrix[i - 1][j - 1] + other

        self.ps = ps

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 += 1
        col2 += 1
        return (
            self.ps[row2][col2]
            - self.ps[row1][col2]
            - self.ps[row2][col1]
            + self.ps[row1][col1]
        )
