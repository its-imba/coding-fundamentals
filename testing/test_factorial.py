from factorial2 import fact

def test_factorial():
    """
    This function tests the factorial function
    """
    x = 10
    expected_result = 3628800
    assert fact(x) == expected_result