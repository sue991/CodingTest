T = int(input())

for m in range(1,T+1):
    lst = list(map(int,input()))
    stk = []
    for i in range(len(lst)):
        if i == 0:
            for _ in range(lst[i]):
                stk.append("(")
            stk.append(lst[i])        
        else:
            if lst[i]>lst[i-1]:
                for _ in range(lst[i]-lst[i-1]):
                    stk.append("(")
                stk.append(lst[i])
            elif lst[i] < lst[i-1]:
                for _ in range(lst[i-1]-lst[i]):
                    stk.append(")")
                stk.append(lst[i])
            else:
                stk.append(lst[i])
        if i == len(lst)-1:
            for _ in range(lst[i]):
                stk.append(")")
    
    print("Case #{0}:".format(m),end=" ")
    for i in stk:
        print(i, end="")
    print("")
