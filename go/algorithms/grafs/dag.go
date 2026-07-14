package graf

var order []int // В этом срезе будет записан порядок обхода.
var dag_color []string

func getOutgoingEdges(v int) []int {
	// Реализация получения исходящих рёбер для вершины v.
	return []int{}
}

func initialize(numVertices int) {
	order = make([]int, 0)
	dag_color = make([]string, numVertices)
	for i := range dag_color {
		dag_color[i] = "white"
	}
}

func topSort(v int) {
	dag_color[v] = "gray"
	outgoingEdges := getOutgoingEdges(v)
	for _, w := range outgoingEdges {
		if dag_color[w] == "white" {
			topSort(w)
		}
	}
	dag_color[v] = "black"
	order = append(order, v) // Кладём обработанную вершину в срез.
}

func mainTopSort() {
	for i := 0; i < len(dag_color); i++ {
		if dag_color[i] == "white" {
			topSort(i)
		}
	}
}

func main_dag() {
	numVertices := 10 // Задайте нужное количество вершин.
	initialize(numVertices)

	mainTopSort()
}
