'''
https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
'''


def find_averages_of_sub_arrays_bf(k, arr):
    # Time Complexity is O(NxK)
    result = []

    l = len(arr)
    for i in range(l - k + 1):
        _sum = 0
        for j in range(i, i + k):
            _sum += arr[j]
        result.append(_sum / k)
    return result


def find_averages_of_sub_arrays(k, arr):
    result = []

    windowSum = 0.0
    windowStart = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:

            result.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result