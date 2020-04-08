T = int(input())

lst = [list(map(int,input().split())) for _ in range(T)]

for lt in lst:
    x = lt[0]
    y = lt[1]

    if (x*y)%2 == 0:
        for i in range(x):
            for j in range(y):
                if i == 0 and j == 0:
                    print("B",end="")
                elif (i+j)%2 == 0:
                    print("W",end="")
                elif (i+j)%2 == 1:
                    print("B",end="")
            print("")
    else:
        for i in range(x):
            for j in range(y):
                if (i+j)%2 == 0:
                    print("B",end="")
                elif (i+j)%2 == 1:
                    print("W",end="")
            print("")