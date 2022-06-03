"""
https://www.educative.io/courses/grokking-the-coding-interview/xog6q15W9GP
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

"""


def pair_with_targetsum(arr, target_sum):
    l, r = 0, len(arr) - 1
    total = 0
    while l <= r:
        total = arr[l] + arr[r]
        if total == target_sum:
            return [l, r]
        elif total > target_sum:
            r -= 1
        else:
            l += 1
    return [-1, -1]


def pair_with_targetsum_hash(arr, target_sum):

    nums = {}
    for i, num in enumerate(arr):
        if (target_sum - num) in nums:
            return [nums[target_sum-num], i]
        else:
            nums[arr[i]] = i

    return [-1, -1]


def pair_with_targetsum_bf(arr, target_sum):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return [i, j]
    return []


print(pair_with_targetsum_hash([1, 2, 3, 4, 6], 6))  # expects [1, 3]
print(pair_with_targetsum_hash([2, 5, 9, 11], 11))  # expects [0, 2]
