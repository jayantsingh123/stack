def maximum_minimum(arr):
    """ given an array arr, find the maximum of minimum over window sizes of different lengths
    e.g. arr =[1,2,3], then minimum of elements over different sizes are given below;
    size 1: 1 ,2, 3. max over all of them is 3
    size 2: 1(minimum over [1,2]), 2(minimum over [2,3]). and maximum is 2
    size 3: 1(minimum over 1,2,3,)  and maximum is 1."""
    from collections import defaultdict
    n = len(arr)
    L = []
    arr2 = [0]*n
    d = defaultdict(int)
    for i in range(n):
        #use the idea of next small as well as previous smaller. element under the top of stack
        # is the previous smaller for the top
        while len(L)>0 and arr[i]<arr[L[-1]]:
            tp=L.pop()
            if len(L)>0:
                size = i-L[-1]-1 #gives the size of window over which arr[tp] is a local minimum

            else:
                size = i  #if no previous small element, then window size is same as i,
                          # where i is index of next smaller
            d[size] = max(d[size], arr[tp]) # find max over all values for same window size
            arr2[size-1] = d[size] #convert the dictionary values to 0 based array, so window size 1 is same as
                                   # first value of arr2
        L.append(i)
    while len(L)>0:
        tp=L.pop()
        if len(L)>0:
            size = n-1-L[-1]
        else:
            size=n
        d[size] = max(d[size], arr[tp])
        arr2[size - 1] = d[size]

    for j in range(n-2,-1,-1):
        arr2[j] = max(arr2[j], arr2[j+1])

    return d, arr2
