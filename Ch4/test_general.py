import pytest
from generalch4 import myList

def test_add_one():
    print('lol')
    assert myList([1,2,3]).addone() == [2,3,4]