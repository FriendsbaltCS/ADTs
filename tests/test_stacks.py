import pytest
from src.stacks import Stack

def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert not stack.is_empty()
    assert stack.peek() == 1

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()

def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    stack.pop()
    assert stack.peek() == 1

def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()