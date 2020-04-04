T = int(input())
for m in range(T):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        lst[i].append(i)
    lst.sort()

    C,J = [],[[-1,-1,-1]]
    ci,ji = 0,0
    for i in range(n):
        if i==0:
            C.append(lst[i])
        else:
            if C[ci][0]<=lst[i][0]<C[ci][1]:
                if lst[i][0] >= J[ji][1]:
                    J.append(lst[i])
                    ji += 1

            elif C[ci][1]<=lst[i][0]:
                C.append(lst[i])
                ci += 1

    for x in C:
        x.append("C")
    for x in J:
        x.append("J")

    ans = []
    for x in C:
        ans.append(x)
    for x in J:
        ans.append(x)

    ans.sort(key = lambda x : x[2])
    print("Case #{0}: ".format(m+1),end="")
    if len(C)+len(J) != n+1:
        print("IMPOSSIBLE",end="")
    else:
        for x in ans[1:]:
            print(x[3],end="")
    print("")


