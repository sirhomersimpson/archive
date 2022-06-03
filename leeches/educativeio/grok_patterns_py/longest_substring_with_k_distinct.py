"""
https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

"""
from collections import defaultdict


def longest_substring_with_k_distinct_bf(str1, k):
    """
    Brute force approach that has TC O(N^2) and SC
    """
    max_length = 0
    # Step 1. generate all substrings of str1
    lst = [str1[i:j] for i in range(len(str1)) for j in range(i + 1, len(str1) + 1)]
    print(lst)
    # Step 2. Find count of distinct elements in str1.
    #   If count == k, find substring length and see if it is maximum
    for l in lst:
        count = len(set(l))
        if count <= k:
            max_length = max(max_length, len(l))
    return max_length


def longest_substring_with_k_distinct(str1, k):
    window_start = 0
    max_length = 0
    char_frequency = {}
    # Step 1. Go through the window
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # Step 2. Add each char in dict
        #char_frequency.setdefault(right_char, 0)
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        
        # Step 3. If distinct chars in dict > K, time to shrink the window
        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1

        # Step 4. Find the distance between window_start and window_end for maximum length
        max_length = max(max_length, window_end - window_start + 1)
      
    return max_length


def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2))) # 4
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1))) # 2
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3))) # 5


main()
