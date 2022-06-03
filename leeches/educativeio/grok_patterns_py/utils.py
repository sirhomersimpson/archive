"""
Utils functions
"""


def generate_substrings(str1):
    my_substrings = []

    my_substrings = [str1[i:j] for i in range(len(str1)) for j in range(i + 1, len(str1) + 1)]
    return my_substrings


def binary_search(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid+1, high, target)
    else:
        return -1


def test_generate_substrings():
    print(generate_substrings("ab"))  # Expects ['a', 'b', 'ab']
    print(generate_substrings("abc"))  # Expects ['a', 'b', 'ab']


def test_binary_search():
    arr = [1, 2, 4, 10]
    target = 4
    print(binary_search(arr, 0, len(arr)-1, target))


def main():
    print("Main function")
    test_binary_search()

main()
