"""

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

"""
from pair_with_targetsum import *


def test_pair_with_targetsum():
    assert pair_with_targetsum([1, 2, 3, 4, 6], 6) == [1, 3]
    assert pair_with_targetsum([2, 5, 9, 11], 11) == [0, 2]


def test_pair_with_targetsum_bf():
    assert pair_with_targetsum_bf([1, 2, 3, 4, 6], 6) == [1, 3]
    assert pair_with_targetsum_bf([2, 5, 9, 11], 11) == [0, 2]


def test_pair_with_targetsum_hash():
    assert pair_with_targetsum_hash([1, 2, 3, 4, 6], 6) == [1, 3]
    assert pair_with_targetsum_hash([2, 5, 9, 11], 11) == [0, 2]
