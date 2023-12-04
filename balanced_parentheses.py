def balanced_parentheses(s):
    """ check if parentheses are balanced,
    means latest opening bracket is closed first
      e.g. '({})' is balanced, but '({)}' is not """
    L = []
    left = ['(', '{', '[']
    right = [')', '}', ']']
    for i in range(len(s)):
        if s[i] in left:
            L.append(s[i])
        else:
            pos = right.index(s[i])
            if len(L) > 0:
                if L[-1] == left[pos]:
                    L.pop()
                else:
                    return 'No'
            else:
                return 'No'
    if len(L) == 0:
        return 'Yes'
    else:
        return 'No'
