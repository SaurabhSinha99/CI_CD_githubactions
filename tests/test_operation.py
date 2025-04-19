from src.math_operation import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(5,3) == 8

def test_sub():
    assert sub(2,3) == -1
    assert sub(5,3) == 2
    assert sub(8,3) == 5
    assert sub(7,3) == 4