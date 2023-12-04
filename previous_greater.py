def previous_greater(arr):
    """ for every element find the next greater
    element on the left"""
    n = len(arr)
    L = []
    d = {}
    L.append(arr[n-1])
    for i in range(n-2,-1,-1):
        while len(L) > 0 and arr[i] > L[-1]:
            x = L.pop()
            d[x] = arr[i]
        L.append(arr[i])
    if len(L)>0:
        for j in range(len(L)):
            d[L[j]] = -1
    return d