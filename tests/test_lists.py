import pytest
from src.lists import OrderedList, UnorderedList

@pytest.mark.parametrize("ListType", [OrderedList, UnorderedList])
def test_append(ListType):
    lst = ListType()
    lst.append(1)
    assert lst.get(0) == 1
    lst.append(2)
    assert lst.get(1) == 2

@pytest.mark.parametrize("ListType", [OrderedList, UnorderedList])
def test_remove(ListType):
    lst = ListType()
    lst.append(1)
    lst.append(2)
    lst.remove(1)
    assert lst.size() == 1
    assert lst.get(0) == 2

@pytest.mark.parametrize("ListType", [OrderedList, UnorderedList])
def test_get(ListType):
    lst = ListType()
    lst.append(1)
    lst.append(2)
    assert lst.get(0) == 1
    assert lst.get(1) == 2

@pytest.mark.parametrize("ListType", [OrderedList, UnorderedList])
def test_size(ListType):
    lst = ListType()
    assert lst.size() == 0
    lst.append(1)
    assert lst.size() == 1
    lst.append(2)
    assert lst.size() == 2
    lst.remove(1)
    assert lst.size() == 1