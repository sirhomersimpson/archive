from remove_element import *


def test_remove_element():
    assert remove_element([2, 11, 2, 2, 1], 2) == 2
    assert remove_element([4, 11, 2, 2, 3], 2) == 3
    assert remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3) == 4
