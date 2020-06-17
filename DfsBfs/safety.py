from collections import deque
import copy
        
def bfs(temp,cnt,x,y,h):
    temp[x][y] = 0
    q = deque()
    q.append((x,y))
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<= nx < n and 0 <= ny < n:
                if temp[nx][ny] != 0 and temp[nx][ny]> h:
                    cnt += 1
                    q.append((nx,ny))
                    temp[nx][ny] = 0
    return cnt

n = int(input())
zone = []
for i in range(n):
    line = list(map(int,input().split(" ")))
    zone.append(line)
max_h = max(map(max,zone))
safe = []

for h in range(max_h):
    temp = copy.deepcopy(zone)
    cnt = 0
    ans = []
    for i in range(n):
        for j in range(n):
            if temp[i][j] > h:
                ans.append(bfs(temp,cnt+1,i,j,h))

    safe.append(len(ans))
print(max(safe))