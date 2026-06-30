package hashed

// Наивная реализация ассоциативного массива

type Pair struct {
	key   interface{}
	value interface{}
}

type Map struct {
	pairs []Pair
}

func (m *Map) Get(key interface{}) interface{} {
	for _, pair := range m.pairs {
		if pair.key == key {
			return pair.value
		}
	}
	return nil // Если пара не найдена, вернем null
}

func (m *Map) Set(key interface{}, value interface{}) {
	for i, pair := range m.pairs {
		if pair.key == key {
			m.pairs[i].value = value
			return
		}
	}
	// Если пара с заданным ключом не найдена, добавим новую пару
	newPair := Pair{key, value}
	m.pairs = append(m.pairs, newPair)
}
