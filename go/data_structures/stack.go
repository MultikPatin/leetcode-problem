package stack

type Stack struct {
	items []string
}

func NewStack() *Stack {
	return &Stack{items: []string{}}
}

func (s *Stack) IsEmpty() bool {
	return len(s.items) == 0
}

func (s *Stack) lastIndex() int {
	return s.Size() - 1
}

func (s *Stack) Size() int {
	return len(s.items)
}

func (s *Stack) Push(item string) {
	s.items = append(s.items, item)
}

func (s *Stack) Pop() string {
	i := s.lastIndex()
	lastItem := s.items[i]
	s.items = s.items[:i]
	return lastItem
}

func (s *Stack) Peek() string {
	return s.items[s.lastIndex()]
}

func main() {
	stack := NewStack()
	stack.Push("apple")
	stack.Push("banana")
	stack.Push("orange")
	stack.Pop()
}
