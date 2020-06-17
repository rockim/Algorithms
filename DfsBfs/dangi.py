from collections import deque


def check_dangi(dangi,cnt,x,y ):
    dangi[x][y] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0<=nx< n and 0<=ny < n:
                if dangi[nx][ny] == 1:
                    cnt += 1
                    q.append((nx,ny))
                    dangi[nx][ny] =0
    return cnt 




n = int(input())
dangi = []
for i in range(n):
    line = list(map(int,input()))
    dangi.append(line)
cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if dangi[i][j] ==1:
            ans.append(check_dangi(dangi,cnt+1,i,j))
print(len(ans))
for i in sorted(ans):
    print(i)
