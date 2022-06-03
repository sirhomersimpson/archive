#!/usr/bin/env python
"""
Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.
ref: https://www.geeksforgeeks.org/find-whether-a-given-number-is-a-power-of-4-or-not/
https://leetcode.com/problems/power-of-four/
"""
def isPowerOfFour_v1(n):
    # Time Complexity is NxOLog(N)
    print('hello')

    if n == 0:
        return False
    while n!=1:
        if n % 4 != 0:
            return False
        n = n // 4
    return True

data = 65
if (isPowerOfFour_v1(data)):
    print(f"Yes {data} is a power of four")
else:
    print(f"No {data} it ain't a power four")
