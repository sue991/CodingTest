n = int(input())

lst = list(map(int,input().split()))

ex_lst = list(set(lst))
nums = []

sums = 0
for i in range(n-1):
    for j in range(i+1,n):
        if sum(lst[i:j+1]) != 0:
            sums += 1

sums += len(ex_lst)

print(sums)


