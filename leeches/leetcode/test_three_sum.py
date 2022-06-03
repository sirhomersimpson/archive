"""

Input : arr[] = {0, -1, 2, -3, 1}
Output : (0 -1 1), (2 -3 1)

Explanation : The triplets with zero sum are
0 + -1 + 1 = 0 and 2 + -3 + 1 = 0

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
"""
from three_sum import *


# todo: Fix test fixtures
def test_find_triplets_brute_force():
	l = (find_triplets_brute_force([0, -1, 1]))
	print(f'hello world {l}')
	pass
