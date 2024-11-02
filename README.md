# Coding Assignment: Abstract Data Types

This project implements four fundamental abstract data types (ADTs): Stack, Queue, OrderedList, and UnorderedList. Each ADT is defined in its respective Python file, and corresponding test cases are provided to ensure functionality.

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

### List

The List ADT provides a dynamic array-like structure. It includes the following methods:
- `append(item)`: Adds an item to the end of the list.
- `remove(item)`: Removes the first occurrence of an item from the list.
- `get(index)`: Returns the item at the specified index.
- `size()`: Returns the number of items in the list.

## Running Tests

To run the tests for this project, ensure you have `pytest` installed. You can install it using pip:

```
pip install pytest
```

Once installed, navigate to the project directory and run the following command:

```
pytest tests/
```

This will execute all the test cases and report any failures or errors.

## Implementation Instructions

1. Implement the `Stack`, `Queue`, and `List` classes in their respective files located in the `src` directory.
2. Write test cases for each method in the corresponding test files located in the `tests` directory.
3. Ensure all tests pass before submission.

Happy coding!