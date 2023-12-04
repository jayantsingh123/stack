def postfix_evaluate(s):
    L=[]
    L1=['-','+','*','/']
    for i in range(len(s)):
        if s[i] not in L1:
            L.append(s[i])
        else:
            x1 = L.pop()
            x2 = L.pop()
            res = eval(str(x2) + s[i] + str(x1))
            L.append(res)
    return L.pop()