"""
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3008/
solution: https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/?ref=rp
Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3
"""


# TC:O(N^2)
def get_length_bf_longest_substr(input_string):
    list_of_strings = generate_all_substrings(input_string)
    list_of_counts = []
    #print(f"[dbg]: list of strings{list_of_strings}")

    for l in list_of_strings:
        if has_unique_chars(l):
            #print(f"uniq str {l}")
            list_of_counts.append(len(l))
    #print(f"[dbg]:counts of all list {list_of_counts}")

    return max(list_of_counts)


def get_length_optimized_substr(input_string):
    s = set()
    l = len(input_string)
    i = 0
    j = 0
    ans = 0
    """ TC O(N)
        sliding window algorithm
        1. start with i,j window.
        2. increase j
        3. if arr[j] does not existing in set, add it
        4. capture size of set and check it is the max currently
        5. if arr[j] exists in set, that means you have a duplicate, increase i+1 and go back to 2
        6. continue till i,j are less that size of arr
    """
    while i < l and j < l:
        if input_string[j] not in s:
            s.add(input_string[j])
            ans = max(ans, j-i+1)
            j = j + 1
        else:
            s.remove(input_string[i])
            i = i + 1
    return ans


def generate_all_substrings(input_string):
    # list comprehension: https://realpython.com/list-comprehension-python/
    # new_list = [expression for member in iterable]
    return [input_string[:index] for index in range(len(input_string))]


# https://www.geeksforgeeks.org/determine-string-unique-characters/
def has_unique_chars(input_string):
    # using the characteristics that sets will have unique characters
    return len(input_string) == len(set(input_string))


def get_size_uniq_substr(list_of_strings):
    return 0


# sliding window - use set
#https://www.tutorialspoint.com/longest-substring-without-repeating-characters-in-python
#https://www.educative.io/edpresso/finding-length-of-longest-substring-without-repeating-characters
#https://github.com/liuhongjiang/leetcode-solutions-python/blob/master/3-Longest-Substring-Without-Repeating
# -Characters.py
def get_length_optimized_longest_substr(input_string):
    return 0


#print(get_length_bf_longest_substr("abcabcbb"))
#print(get_length_bf_longest_substr("bbbbb"))
print(get_length_bf_longest_substr("abcabcbb"))
print(get_length_optimized_substr("abcabcbb"))
