'''
https://www.dailycodingproblem.com/solution/556?token=287b01148a1ddbaad6efbf029aedc1b166c60a234fee8bbf1d25f3a2cc9402da93b7aaf3
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array
'''
def is_sorted(lst):

    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True


# main
arr = [10, 2, 122]
print(f"is sorted: {is_sorted(arr)}")
arr = [1, 2, 3]
print(f"is sorted: {is_sorted(arr)}")

