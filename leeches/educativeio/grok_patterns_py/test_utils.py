from utils import *


def test_generate_substrings():

	list_str1 = ["a", "abc", "abcd"]
	for str1 in list_str1:
		list_substrings_of_str1 = generate_substrings(str1)
		for s in str1:
			assert s in list_substrings_of_str1
