from itertools import combinations
nn = []
while True:
    n = list(map(int,input().split(" ")))
    if n[0] == 0:
        break
    else:
        nn.append(n)
for k in nn:
    a=[]
    for i in range(1,len(k)):
        a.append(k[i])
    ans = list(combinations(a,6))
    for j in ans:
        print("%d %d %d %d %d %d" % j)
    if k != nn[-1]:
        print()
