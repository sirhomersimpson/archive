from product_all_other_elements import products


def test_products():
    assert products([1, 2, 3]) == [6, 3, 2]

    assert products([0, 0, 0]) == [0, 0, 0]

    assert products([0, 0, -1]) == [0, 0, 0]

    assert products([-2, -3, -1]) == [3, 2, 6]
