import pytest
from src.queues import Queue

def test_enqueue():
    q = Queue()
    q.enqueue(1)
    assert not q.is_empty()
    assert q.front() == 1

def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.front() == 2

def test_front():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.front() == 1
    q.dequeue()
    assert q.front() == 2

def test_is_empty():
    q = Queue()
    assert q.is_empty()
    q.enqueue(1)
    assert not q.is_empty()
    q.dequeue()
    assert q.is_empty()