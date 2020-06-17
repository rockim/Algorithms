from collections import deque

def bfs(box,n,m,t):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q= deque()
    for i in t:
        (cx,cy) = i
        q.append(i)
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0<=nx<m and 0<=ny<n:
                if box[nx][ny]==0:
                    box[nx][ny] = box[x][y] + 1
                    q.append((nx,ny))
a = input().split(" ")
n, m = [int(i) for i in a]
box = []
for i in range(m):
    line = list(map(int,input().split(" ")))
    box.append(line)
temp = []
for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            temp.append((i,j))
bfs(box,n,m,temp)

for i in box:
    if 0 in i:
        zero = 1
        break
    zero = 0
if zero==1:
    print(-1)
else:
    if max(map(max,box))-1<=0:
        print(0)
    else:
        print(max(map(max,box))-1)