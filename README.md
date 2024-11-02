# Coding Assignment: Abstract Data Types

This assignment implements four fundamental abstract data types (ADTs): Stack, Queue, OrderedList, and UnorderedList. Each ADT is defined in its respective Python file, and corresponding test cases are provided to ensure functionality.

## Project Structure

```
coding-assignment
├── src
│   ├── stacks.py      # Stack ADT implementation
│   ├── queues.py      # Queue ADT implementation
│   └── lists.py       # List ADT implementation
├── tests
│   ├── test_stacks.py # Tests for Stack ADT
│   ├── test_queues.py # Tests for Queue ADT
│   └── test_lists.py  # Tests for List ADT
└── README.md          # Project documentation
```

## Abstract Data Types

### Stack

The Stack ADT follows the Last In First Out (LIFO) principle. It includes the following methods:
- `push(item)`: Adds an item to the top of the stack.
- `pop()`: Removes and returns the item from the top of the stack.
- `peek()`: Returns the item at the top of the stack without removing it.
- `is_empty()`: Checks if the stack is empty.

### Queue

The Queue ADT follows the First In First Out (FIFO) principle. It includes the following methods:
- `enqueue(item)`: Adds an item to the back of the queue.
- `dequeue()`: Removes and returns the item from the front of the queue.
- `front()`: Returns the item at the front of the queue without removing it.
- `is_empty()`: Checks if the queue is empty.


### OrderedList

The OrderedList ADT provides a dynamic array-like structure where elements are maintained in a sorted order. It includes the following methods:
- `add(item)`: Adds an item to the list while maintaining order.
- `remove(item)`: Removes the first occurrence of an item from the list.
- `search(item)`: Searches for an item in the list.
- `is_empty()`: Checks if the list is empty.
- `size()`: Returns the number of items in the list.
- `index(item)`: Returns the index of the item in the list.
- `pop()`: Removes and returns the last item in the list.
- `pop(pos)`: Removes and returns the item at the specified position.

### UnorderedList

The UnorderedList ADT provides a dynamic array-like structure. It includes the following methods:
- `add(item)`: Adds an item to the list.
- `remove(item)`: Removes the first occurrence of an item from the list.
- `search(item)`: Searches for an item in the list.
- `is_empty()`: Checks if the list is empty.
- `size()`: Returns the number of items in the list.
- `append(item)`: Adds an item to the end of the list.
- `index(item)`: Returns the index of the item in the list.
- `insert(pos, item)`: Inserts an item at the specified position.
- `pop()`: Removes and returns the last item in the list.
- `pop(pos)`: Removes and returns the item at the specified position.


## Implementation Instructions

1. Implement the `Stack`, `Queue`, and both list classes in their respective files located in the `src` directory.
2. Write test cases for each method in the corresponding test files located in the `tests` directory.
3. Ensure all tests pass before submission.

Happy coding!