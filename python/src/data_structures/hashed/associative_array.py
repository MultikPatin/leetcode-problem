# Наивная реализация ассоциативного массива


class Map[K, V]:
    def __init__(self) -> None:
        self.pairs = []

    def get(self, key: K) -> V | None:
        for pair in self.pairs:
            if pair.key == key:
                return pair.value
        return None  # Если пара не найдена, вернем null

    def set(self, key: K, value: V) -> None:
        for pair in self.pairs:
            if pair.key == key:
                pair.value = value
                return
        # Если пара с заданным ключом не найдена, добавим новую пару
        new_pair = Pair(key, value)
        self.pairs.append(new_pair)


class Pair[K, V]:
    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value
