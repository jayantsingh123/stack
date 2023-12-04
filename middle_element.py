def middle_element(s):
    """ delete mid elemnt of stack
    where mid = (size-1)//2"""
    # keep on moving from right to left and
    # shift the elements until we reach mid

    size = len(s)
    mid = (size-1) // 2
    i = size-1
    temp1 = s[i]
    while i > mid:
        temp = s[i-1]
        s[i-1] = temp1
        temp1 = temp
        i += 1
    s.pop()
    return s