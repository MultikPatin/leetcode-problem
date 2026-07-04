# Подходит для поиска кратчайших путей между всеми парами вершин.
# Он работает на основе матрицы расстояний,
# которая представляет собой квадратную таблицу, где элемент на пересечении строки
# i и столбца j показывает текущее минимальное расстояние от вершины i до вершины j.
# Постепенно обновляя значения в этой таблице,
# алгоритм находит минимальные пути между всеми парами вершин.

# При этом алгоритм способен обрабатывать графы с отрицательными весами рёбер,
# хотя его сложность O(V3)
# делает его менее эффективным для очень больших сетей.

import numpy as np


def floyd_warshall(graph: list[list[int | float]]) -> np.ndarray:
    num_vertices = len(graph)
    dist = np.array(graph)

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Пример использования
graph = [
    [0, 3, float("inf"), 5],
    [2, 0, float("inf"), 4],
    [float("inf"), 1, 0, float("inf")],
    [float("inf"), float("inf"), 2, 0],
]

shortest_paths = floyd_warshall(graph)
print(shortest_paths)
