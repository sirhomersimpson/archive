# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse1(self, x: int) -> int:
        if x < 0:
            x = x * -1
            return int(str(x)[::-1]) * -1
        return int(str(x)[::-1])

    def reverse(self, x):

        negative = x < 0

        if negative:
            x *= -1

        reverse = 0
        while (x > 0):
            reverse = (reverse * 10) + x % 10
            x = x // 10

        if negative:
            reverse *= -1

        if reverse >= 2 ** 31 or reverse <= -2 ** 31:
            return 0

        return reverse


print(Solution().reverse(-123))
print(Solution().reverse(123))
print(Solution().reverse(1534236469))
