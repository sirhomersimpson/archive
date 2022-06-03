from max_sub_array_of_size_k import *


def test_max_sub_array_of_size_k():
    input_list = [2, 3, 4, 1, 5]
    k = 2
    expected = 7

    assert expected == max_sub_array_of_size_k_bf(k, input_list)


def test_max_sub_array_of_size_k_sliding_window():
    input_list = [2, 3, 4, 1, 5]
    k = 2
    expected = 7

    assert expected == max_sub_array_of_size_k_sliding_window(k, input_list)


def test_max_sub_array_of_size_k_sliding_window_data2():
    input_list = [2, 1, 5, 1, 3, 2]
    k = 3
    expected = 9

    assert expected == max_sub_array_of_size_k_sliding_window(k, input_list)
