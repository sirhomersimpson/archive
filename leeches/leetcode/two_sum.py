# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    @staticmethod
    def bf_two_sum(nums: List[int], target: int) -> List[int]:
        l: List = []
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[1:]):
                print(f"a: {a} b: {b}")
                if a + b == target:
                    l.append(a)
                    l.append(b)
        return l


# driver code
my_list = [1, 2, -3, 3]
s = input("name:")
print("your name is: ", s)
print(Solution.bf_two_sum(my_list, 0))
