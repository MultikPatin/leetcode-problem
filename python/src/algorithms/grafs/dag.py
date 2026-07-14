# Топологическая сортировка ориентированного графа —
# это такое упорядочивание всех вершин этого графа,
# что если существует ребро (v,w), то в итоговой последовательности
# v располагается раньше, чем w. Из этого определения можно вывести следствие:
# если в графе есть путь из некоторой вершины s до некоторой другой вершины t,
# то топологическая сортировка должна поставить
# s раньше, чем t.

from src.data_structures.stack import Stack

order = Stack()  # В этом стеке будет записан порядок обхода.
color = ["white", "white", "white"]  # Пример заполнения значением 'white'


def top_sort(v: int) -> None:
    color[v] = "gray"
    outgoing_edges = get_outgoing_edges(v)
    for w in outgoing_edges:
        if color[w] == "white":
            top_sort(w)
    color[v] = "black"
    order.push(v)  # Кладём обработанную вершину в стек.


def main_top_sort() -> None:
    for i in range(len(color)):
        if color[i] == "white":
            top_sort(i)


def get_outgoing_edges(v: int) -> list[int]:
    # Реализация получения исходящих рёбер для вершины v
    return []


# Пример использования
main_top_sort()
