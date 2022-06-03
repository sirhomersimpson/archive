from find_averages_of_subarrays import find_averages_of_sub_arrays_bf
from find_averages_of_subarrays import find_averages_of_sub_arrays


def test_find_averages_of_sub_arrays_bf():
    result = find_averages_of_sub_arrays_bf(2, [1, 2, 3])
    expected_result = [1.5, 2.5]
    assert expected_result == result

    result = find_averages_of_sub_arrays_bf(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    expected_result = [2.2, 2.8, 2.4, 3.6, 2.8]
    assert expected_result == result


def test_find_averages_of_sub_arrays():
    result = find_averages_of_sub_arrays(2, [1, 2, 3])
    expected_result = [1.5, 2.5]
    assert expected_result == result

    result = find_averages_of_sub_arrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    expected_result = [2.2, 2.8, 2.4, 3.6, 2.8]
    assert expected_result == result
