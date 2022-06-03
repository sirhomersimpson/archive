# https://www.codeproject.com/Tips/1275693/Recursive-Permutations-in-Python
# Recursive implementation of permutations. Time complexity is N! (But some book say it is N^2*N!
# Note that itertools permutations is anecdotally 7 times faster than this approach
from itertools import permutations
import time
import random
import string
from itertools import permutations

def permute_recursive(s):
	
	out = []
	# Base case:
	if len(s) == 1:
		return s
	
	for i, pref in enumerate(s):
		# s[:i] + s[i+1:] we skip s[i] as it is the prefix
		# e.g s="abc" - prefix=b, P(a..c)
		for perm in permute_recursive(s[:i] + s[i+1:]):
			out += [pref + perm]

	return out


def permute_iter(s):
	lst = []
	
	for perm in permutations(s):
		lst.append(perm)
	return lst

def load_test (k):
	
	#Choose a random string
	str1 = random.choices(string.ascii_lowercase, k=k)
	print(str1)
	print("Starting Recursive permutation")
	start_time = time.time()
	#print(permute_recursive(str1))
	permute_recursive(str1)
	end_time = time.time()
	diff_recur = end_time - start_time
	print(f'(Permute Recursive) Elapsed time {diff_recur} seconds')
	
	print("Starting Itertools permutation")
	start_time = time.time()
	#print(permute_recursive(str1))
	permute_iter(str1)
	end_time = time.time()
	diff_iter = end_time - start_time
	print(f'(Itertools Itertools) Elapsed time {diff_iter} seconds')

	diff = diff_recur-diff_iter
	diff_percent = (diff / (diff_recur)) * 100
	print('Summary (itertools is faster than recursive by ): {0:.5f} seconds'.format(diff))
	print('Summary (itertools is faster than recursive by ): {0:.2f} %'.format(diff_percent))


# Load tests . it will run iterations times for
# for arrays from start i and j
iterations = 1
start_arr_length = 10
end_arr_length = 12
for i in range(start_arr_length, end_arr_length):
	print(f'Load Test with load {i} running {iterations} times')
	for j in range(iterations):
		load_test(i)
