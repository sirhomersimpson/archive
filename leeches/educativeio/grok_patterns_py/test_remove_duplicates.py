from remove_duplicates import *


def test_remove_duplicates():

    assert remove_duplicates([2, 3, 3, 3, 6, 9, 9]) == 4
    assert remove_duplicates([2, 2, 2, 11]) == 2
