from non_repeat_substring import *


def test_non_repeat_substring():
    #assert non_repeat_substring("aabccbb") == 3
    assert non_repeat_substring("abbbb") == 2
    #assert non_repeat_substring("abccde") == 3


def test_non_repeat_substring_bf():
    assert non_repeat_substring_bf("aabccbb") == 3
    assert non_repeat_substring_bf("abbbb") == 2
    assert non_repeat_substring_bf("abccde") == 3


def test_is_unique():
    assert contains_unique_chars("aabccbb") == False
    assert contains_unique_chars("abc") == True
    assert contains_unique_chars("a") == True
    assert contains_unique_chars("") == True
