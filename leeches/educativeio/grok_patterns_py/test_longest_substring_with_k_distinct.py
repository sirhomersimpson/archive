from longest_substring_with_k_distinct import *


def test_longest_substring_with_k_distinct():

    assert 2 == longest_substring_with_k_distinct("aabbcc", 1)
    assert 2 == longest_substring_with_k_distinct("araaci", 1)
    assert 5 == longest_substring_with_k_distinct("cbbebi", 3)


def test_longest_substring_with_k_distinct_bf():

    assert 2 == longest_substring_with_k_distinct_bf("aabbcc", 1)
    assert 2 == longest_substring_with_k_distinct_bf("araaci", 1)
    assert 5 == longest_substring_with_k_distinct_bf("cbbebi", 3)


