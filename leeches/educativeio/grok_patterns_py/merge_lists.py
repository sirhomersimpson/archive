#!/bin/env python3
"""
https://www.educative.io/module/lesson/data-structures-in-python/39Vv2YVxxVx
Non in place
TC O(n)
SC O(n)
"""
def merge_lists(l1, l2):
    index1, index2, index_result = 0,0,0
    result = []

    for i in range(len(l1) + len(l2)):
        result.append(i)
    
    while (index1 < len(l1)) and (index2<len(l2)):
        if l1[index1] < l2[index2]:
            result[index_result] = l1[index1]
            index_result += 1
            index1 += 1
        else:
            result[index_result] = l2[index2]
            index_result += 1
            index2 += 1

    while index1 < len(l1):
        result[index_result] = l1[index1]
        index_result += 1
        index1 += 1

    while index2 < len(l2):
        result[index_result] = l2[index2]
        index_result += 1
        index2 += 1
    
    return result

print(merge_lists([1,5,12], [0,5,33]))
    
