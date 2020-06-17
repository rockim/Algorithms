from collections import deque

def bfs(buat, x,y,cnt):
    buat[x][y]= 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    q.append((x,y))    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0<=nx<sero and 0<=ny<garo:
                if buat[nx][ny] == 1:
                    buat[nx][ny] = 0
                    cnt+=1
                    q.append((nx,ny))
    return cnt
n = int(input())
    

for i in range(n):
    n_input = input().split(" ")
    garo,sero,bugs = [int(j) for j in n_input]
    buat = [[0] * garo for j in range(sero)]
    for bug in range(bugs):
        b = input().split(" ")
        b_garo, b_sero = [int(j) for j in b]
        buat[b_sero][b_garo] = 1
    ans = []
    cnt = 0
    for x in range(sero):
        for y in range(garo):
            if buat[x][y] == 1:
                ans.append(bfs(buat,x,y,cnt+1))
    print(len(ans))