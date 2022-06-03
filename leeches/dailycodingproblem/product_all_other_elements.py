## Problem 1.1 Get Product of all elements
def products(nums):
    prefix = [1]
    for index in range(1, len(nums)):
        prod = nums[index-1] * prefix[-1]
        prefix.append(prod)

    #print(prefix)
    suffix = [1]
    reverse_nums = list(reversed(nums))
    for index in range(1, len(reverse_nums)):
        prod = reverse_nums[index-1] * suffix[-1]
        suffix.append(prod)
    suffix = list(reversed(suffix))
    #print(suffix)

    final_lst = []
    for index in range(len(nums)):
        final_lst.append(prefix[index] * suffix[index])

    return final_lst


print(products([1, 2, 3, 4, 5]))
