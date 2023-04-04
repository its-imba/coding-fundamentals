from count import count

def test_count_integers():
    """"
    This function tests the count with a list of integers
    """
    sequence = [1,2,3,4,5,4,6,4,7,4,1,4]
    item = 4
    expected_result = 5
    assert count(sequence, item) == expected_result

def test_count_strings():
    """
    This function tests the count with a list of strings
    """
    sequence = ['cat', 'dog', 'cat', 'bird', 'cat', 'pig']
    item = 'cat'
    expected_result = 3
    assert count(sequence, item) == expected_result
