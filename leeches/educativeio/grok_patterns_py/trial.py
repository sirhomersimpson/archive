# https://www.codeproject.com/Tips/1275693/Recursive-Permutations-in-Python
def permute(s):
    out = []
    if len(s) == 1:
        return s
    else:
        for i, let in enumerate(s):
            print(s[:i] + "XXXX" + s[i+1:])
            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]
    return out


print(permute('ab'))
