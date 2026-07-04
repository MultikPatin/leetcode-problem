# Позволяет находить кратчайшие пути от заданной вершины до всех остальных,
# даже если в графе присутствуют отрицательные веса рёбер.
# Однако алгоритм лучше применять для средних по размеру графов,
# поскольку его временная сложность составляет O(VE), где:
# V — количество вершин в графе,
# E — количество рёбер в графе.


def bellman_ford(
    graph: dict[str, list[tuple[str, int]]], source: str
) -> dict[str, float]:
    distance = {vertex: float("inf") for vertex in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight

    # Проверка на отрицательные циклы
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distance[vertex] + weight < distance[neighbor]:
                msg = f"Отрицательный цикл: {vertex} -> {neighbor} -> {vertex}"
                raise ValueError(msg)

    return distance


# Пример использования
graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", -1), ("D", 2)],
    "C": [("D", 3)],
    "D": [],
}

distances = bellman_ford(graph, "A")
print(distances)  # {'A': 0, 'B': 4, 'C': 2, 'D': 5}
