from calculator import add

def test_add():
    # Verify that the add function correctly adds two numbers
    assert add(2, 3) == 5
    assert add(-1, 1) == 0