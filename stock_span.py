def stock_span(arr):
    """ for every element elem in arr, fnd count of consecutive
    elements on left side which are not greater than elem. We can include
    elem"""
   # from collections import OrderedDict
    arr2 = arr.copy()
    n = len(arr)
    dnew = {}
    arr.reverse()
    L= []
    Lnew=[0]*n

   # d = OrderedDict()
    for i in range(n):
        while len(L)>0 and L[-1][0]<arr[i]:
            elem = L.pop()
            Lnew[elem[1]] = elem[1]-(n-1-i)
            #dnew[(elem[0],elem[1])]= (arr[i],n-1-i)
        L.append((arr[i],n-1-i))
    for k in L:
        Lnew[k[1]] = k[1]+1

    #while len(L)>0:
     #   elem=L.pop()
      #  dnew[(elem[0], elem[1])]=tuple()
    #for k,v in enumerate(arr2):

     #   if len (dnew[v,k]) > 0:
      #      Lnew.append(k - dnew[v,k][1])
       # else:
        #    Lnew.append(k+1)

    return Lnew
   # return Lnew
