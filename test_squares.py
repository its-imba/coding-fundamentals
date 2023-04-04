from list_of_squares import list_of_squares

def test_square_count():
    """
    This function tests if the list of squares is returned correctly
    """
    n = 100
    expected_result = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961]
    assert list_of_squares(n) == expected_result