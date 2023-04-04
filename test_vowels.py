from vowels import vowels

def test_vowel_count():
    """
    This function tests that the vowels are counted correctly
    """
    word = "alphabet"
    the_vowels = ["a", "e", "i", "o", "u"]
    expected_result = 3
    assert vowels(word) == expected_result


