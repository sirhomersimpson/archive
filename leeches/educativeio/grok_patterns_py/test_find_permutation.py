from find_permutation import *


def test_find_permutation():
	assert find_permutation("oidbcaf", "abc") == True
	assert find_permutation("aba", "bc") == False
