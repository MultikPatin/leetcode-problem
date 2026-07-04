import heapq

# В данной реализации граф представлен в виде словаря смежности.
# Это словарь, где ключами являются вершины, а значениями —
# списки пар (соседняя_вершина, вес_ребра).
# Такой способ удобен в Python, особенно когда вершины имеют строковые имена.
# Он эквивалентен списку смежности,
# но предоставляет более удобный доступ к элементам.


def dijkstra(
    graph: dict[str, list[tuple[str, int]]], start: str
) -> dict[str, float]:
    distance = {vertex: float("inf") for vertex in graph}
    distance[start] = 0
    priority_queue = [(0, start)]  # (расстояние, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если найден более короткий путь, пропускаем
        if current_distance > distance[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance_to_neighbor = current_distance + weight

            if distance_to_neighbor < distance[neighbor]:
                distance[neighbor] = distance_to_neighbor
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

    return distance


# Пример использования
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": [],
}

distances = dijkstra(graph, "A")
print(distances)  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
