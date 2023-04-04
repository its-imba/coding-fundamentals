from list_of_squares import list_of_squares

def test_square_count():
    """
    This function tests if the list of squares is returned correctly
    """
    n = 6
    expected_result = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
    assert list_of_squares(n) == expected_result