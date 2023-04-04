"""This program counts"""
def count(sequence, item):
    """
    This function counts the number of times an item appears in a sequence.
    """
    counter = 0
    for num in sequence:
        if num == item:
            counter += 1
    return counter
