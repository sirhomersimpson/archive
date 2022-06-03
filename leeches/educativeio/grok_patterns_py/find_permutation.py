"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.

"""
from itertools import permutations
import pprint


def find_permutation_bf(str1, pattern):
	
	# Step 1 - Generate all permutations
	lst = list(permutations(str1))
	# Step 2 - Convert each list in lst to a string for easy comparison
	lst2 = []
	for l in lst:
		lst2.append("".join(l))
	#pprint.pprint(lst2)
	# Step 3 - iterate through list version of permutation and check if pattern is part of it
	for l in lst2:
		#pprint.pprint(l)
		if pattern in l:
			return True
		
	return False


def find_permutation(str1, pattern):
	window_start, matched = 0, 0
	char_frequency = {}
	
	for chr in pattern:
		if chr not in char_frequency:
			char_frequency[chr] = 0
		char_frequency[chr] += 1
	
	# our goal is to match all the characters from the 'char_frequency' with the current window
	# try to extend the range [window_start, window_end]
	for window_end in range(len(str1)):
		right_char = str1[window_end]
		if right_char in char_frequency:
			# decrement the frequency of matched character
			char_frequency[right_char] -= 1
			if char_frequency[right_char] == 0:
				matched += 1
		
		if matched == len(char_frequency):
			return True
		
		# shrink the window by one character
		if window_end >= len(pattern) - 1:
			left_char = str1[window_start]
			window_start += 1
			if left_char in char_frequency:
				if char_frequency[left_char] == 0:
					matched -= 1
				char_frequency[left_char] += 1
	
	return False


def main():
	print('Permutation exist: ' + str(find_permutation_bf("abcd", "z")))  # Expects False
	print('Permutation exist: ' + str(find_permutation_bf("oidbcaf", "abc"))) # Expects True
	print('Permutation exist: ' + str(find_permutation("odicf", "dc"))) # Expects False
	print('Permutation exist: ' + str(find_permutation_bf("bcdxabcdy", "bcdyabcdx"))) # Expects True
	print('Permutation exist: ' + str(find_permutation_bf("aaacb", "abc"))) # Expects  True


main()
