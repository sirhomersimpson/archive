#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:

    def twoSum_bf(self, numbers: List[int], target: int) -> List[int]:
        #brute-force, TC = O(N^2)
        size = len(numbers)
        for i in range(size-1):
            for j in range(size):
                sum = numbers[i] + numbers[j]
                if sum == target:
                    return [i, j]

        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #optimized solution, TC = O(N)
        low = 0
        high = len(numbers)-1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low, high]
            elif sum < target:
                low += 1
            else:
                high -= 1
        return []

#main


l = [10, 23, 1, 5, 100]
l.sort()
print(l)
#value = Solution().twoSum_bf(l, 11)
value = Solution().twoSum(l, 11)

print(value)
