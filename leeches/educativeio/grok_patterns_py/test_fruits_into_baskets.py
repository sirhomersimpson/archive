from fruits_into_baskets import fruits_into_baskets


def test_fruits_into_baskets():
    assert fruits_into_baskets(['A', 'B', 'C', 'A', 'C']) == 3
    assert fruits_into_baskets(['B', 'C', 'B', 'B', 'C']) == 5
