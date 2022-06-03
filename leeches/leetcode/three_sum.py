"""

https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""


def find_triplets_brute_force(arr):
	
	my_list = []
	for i in range(len(arr)-2):
		for j in range(i+1, len(arr)-1):
			for k in range(j+1, len(arr)):
				if arr[i] + arr[j] + arr[k] == 0:
					#print(f'found it: {i} {j} {k}')
					my_list.append([arr[i], arr[j], arr[k]])
	return my_list


print(find_triplets_brute_force([-1, 0, 1, 2, -1, -4]))
