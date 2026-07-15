from queue import Queue

# Длины массивов равны числу вершин |V|.
color = ["white", "white", "white"]  # Пример заполнения значением 'white'
previous = [None, None, None]  # Пример заполнения значением None
distance = [None, None, None]  # Пример заполнения значением None


def bfs(s):
    # Создадим очередь вершин и положим туда стартовую вершину.
    planned = Queue()
    planned.put(s)
    color[s] = "gray"
    distance[s] = 0
    while not planned.empty():
        u = planned.get()  # Возьмём вершину из очереди.
        for v in outgoing_edges(u):
            if color[v] == "white":  # Серые и чёрные вершины уже
                # либо в очереди, либо обработаны.
                distance[v] = distance[u] + 1
                previous[v] = u
                color[v] = "gray"
                planned.put(v)  # Запланируем посещение вершины.
        color[u] = "black"  # Теперь вершина считается обработанной.


def shortest_path(v):
    # Класть вершины будем в стек, тогда
    # стартовая вершина окажется наверху стека
    # и порядок следования от s до v будет соответствовать
    # порядку извлечения вершин из стека.
    path = []
    current_vertex = v
    while current_vertex is not None:  # Предшественник вершины s равен None.
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    return path


def outgoing_edges(u):
    # Реализация получения исходящих рёбер для вершины u.
    pass
