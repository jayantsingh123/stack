def largest_area(arr):

    """ return indices of smaller element for every
     array element on left as well as right.
     e.g arr=[2,4,1,5] dleft ={ 2: -1, 4:0, 1:-1, 5:2}
     Here -1 signifies, there is no smaller element on the left """

    #from collections import defaultdict
    n = len(arr)
    left_area, right_area = [0]*n, [0]*n
    res, area = -999, 0
    left, right = [-1]*n, [-1]*n
    left_stack, right_stack = [], []
    # find the index of first smaller element on the left
    for j in range(n-1, -1, -1):
        while len(left_stack) > 0 and arr[j] < left_stack[-1][1]:
            x = left_stack.pop()
            left[x[0]] = j

        left_stack.append((j, arr[j]))


    for k in range(0, n):
        while len(right_stack) > 0 and arr[k] < right_stack[-1][1]:
            x = right_stack.pop()
            right[x[0]] = k

        right_stack.append((k, arr[k]))

    for i in range(0, n):
        if left[i] == -1:
            left_area[i] = (i+1)*arr[i]
        else:
            left_area[i] = (i-left[i])*arr[i]
    for l in range(n):
        if right[l] == -1:
            right_area[l] = (n-1-l)*arr[l]
        else:
            right_area[l] = (right[l] - (l+1)) * arr[l]
    for i in range(n):
        area = left_area[i]+right_area[i]
        #print(area)
        res = max(area, res)
    #print(left_area, right_area)



    return res
