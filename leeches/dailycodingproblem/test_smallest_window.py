from smallest_window import window


def test_window_test_case1():
    t = (1, 3)
    assert (window([3, 7, 5, 6, 9]) == t)


def test_window_test_case2():
    t = (0, 3)
    assert (window([9, 6, 5, 1]) == t)