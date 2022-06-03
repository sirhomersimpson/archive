#https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/308/


def divide(dividend, divisor):
    """
    TC ~ O(N)
    """
    count = 0
    diff = 0
    is_a_neg = False
    if dividend < 0 or divisor < 0:
        is_a_neg = True
    # Make all numbers absolute to capture negative numbers
    dividend = abs(dividend)
    divisor = abs(divisor)
    while count >= 0:
        diff = dividend - divisor
        dividend = diff
        if diff < 0:
            # hack if we are dealing with -ve numbers
            count = -count if is_a_neg else count
            return count
        count = count + 1
    return count


print(divide(10, 7))
print(divide(10, 3))
print(divide(10, -3))

