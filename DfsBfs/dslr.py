from collections import deque

def bfs(a):
    q.append([a,""])
    num[a] = 1
    while q:
        a,d = q.popleft()
        if  a == b:
            return d
        if 2*a < 10000 and num[2*a] == 0:
            num[2*a] = 1
            q.append([2*a,d+'D'])
        if 2*a >= 10000 and num[(2*a)%10000]==0:
            num[(2*a)%10000] = 1
            q.append([(2*a)%10000,d+"D"])
        if a - 1 >=0 and num[a-1] == 0:
            num[a-1]=1
            q.append([a-1,d+"S"])
        if a-1< 0 and num[9999]==0:
            num[9999]=1
            q.append([9999,d+'S'])
        na = int((a%1000)*10 + a/1000)
        if num[na] == 0:
            num[na] = 1
            q.append([na,d+'L'])
        na = int((a%10) * 1000 + a /10)
        if num[na]==0:
            num[na] = 1
            q.append([na,d+'R'])

n = int(input())
while n:
    num = [0 for i in range(10000)]
    q = deque()
    a,b = [int(j) for j in input().split(" ")]
    print(bfs(a))
    n -= 1
