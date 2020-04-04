T = int(input())

for m in range(1,T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for i in range(n)]
    k,r,c = 0,0,0
    for i in range(n):
        k += matrix[i][i]
        new_list_row = []
        for v in matrix[i]:
            if v not in new_list_row:
                new_list_row.append(v)
        if len(new_list_row) != n:
            r += 1
        new_list_col = []
        for j in range(n):
            if matrix[j][i] not in new_list_col:
                new_list_col.append(matrix[j][i])
        if len(new_list_col) != n:
            c += 1

    print("Case #{0}:".format(m),k,r,c)