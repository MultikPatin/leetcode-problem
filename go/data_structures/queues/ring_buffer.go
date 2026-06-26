package queues

type RingBufferQueue struct {
	queue []any
	maxN  int
	head  int
	tail  int
	size  int
}

func NewRingBufferQueue(n int) *RingBufferQueue {
	return &RingBufferQueue{
		queue: make([]any, n),
		maxN:  n,
		head:  0,
		tail:  0,
		size:  0,
	}
}

func (q *RingBufferQueue) IsEmpty() bool {
	return q.size == 0
}

func (q *RingBufferQueue) Push(x any) {
	if q.size != q.maxN {
		q.queue[q.tail] = x
		q.tail = (q.tail + 1) % q.maxN
		q.size += 1
	}
}

func (q *RingBufferQueue) Pop() any {
	if q.IsEmpty() {
		return nil
	}
	x := q.queue[q.head]
	q.queue[q.head] = nil
	q.head = (q.head + 1) % q.maxN
	q.size -= 1
	return x
}
