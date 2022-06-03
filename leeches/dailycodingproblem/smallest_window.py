def window(array):
    l, r = None, None
    s = sorted(array)

    for i in range(len(array)):
        if array[i] != s[i] and l is None:
            l = i
        elif array[i] != s[i]:
            r = i
    print(f'{l} {r}')
    return l, r


a = window([3, 7, 5, 6, 9])
print(a)
