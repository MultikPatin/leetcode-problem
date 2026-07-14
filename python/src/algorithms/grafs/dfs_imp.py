from enum import StrEnum
from typing import Protocol


class VertexColor(StrEnum):
    WHITE = "white"
    GRAY = "gray"
    BLACK = "black"


class Graph(Protocol):
    def outgoing_edges(self, v: int) -> list[int]: ...
    def get_vertex_count(self) -> int: ...


vertex_colors: list[VertexColor] = []


def dfs(graf: Graph, v: int) -> None:
    vertex_colors[v] = VertexColor.GRAY
    for w in graf.outgoing_edges(v):
        if vertex_colors[w] == VertexColor.WHITE:
            dfs(graf, w)
    vertex_colors[v] = VertexColor.BLACK


def main(graf: Graph) -> None:
    vertex_count = graf.get_vertex_count()
    vertex_colors = [VertexColor.WHITE] * vertex_count

    for i in range(vertex_count):
        if vertex_colors[i] == VertexColor.WHITE:
            dfs(graf, i)
