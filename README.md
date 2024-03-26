# Fibonacci Heap

This is a simple implementation of a Fibonacci Heap in Python. It is not optimized for performance, but rather for readability and simplicity. It is intended to be used as a learning tool.

## Variations

1. **FibonacciHeap**: A simple implementation of a Fibonacci Heap.
2. **FibonacciHeapLazy**: A lazy implementation of a Fibonacci Heap. The difference is that the deletion of a node is done lazily, i.e. the node is marked as deleted and is removed from the heap only when it is accessed again.

## Usage

```python
from fibonacci_heap import FibonacciHeap

heap = FibonacciHeap()

# Insert elements
heap.insert(1)
heap.insert(2)
heap.insert(3)

# Get minimum element
print(heap.find_min().val) # 1
```
