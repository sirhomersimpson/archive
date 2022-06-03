from find_smallest_subarray_with_given_sum import smallest_subarray_with_given_sum


def test_smallest_subarray_with_given_sum():
    assert(2 == smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
    assert(1 == smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
    assert(3 == smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))
    assert(0 == smallest_subarray_with_given_sum(2, [1]))

