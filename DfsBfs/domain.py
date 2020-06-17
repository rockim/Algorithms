from collections import deque

def check_wide(square,cnt,x,y):
    square[x][y] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0<=nx<m and 0<=ny<n:
                if square[nx][ny] == 0:
                    cnt += 1
                    q.append((nx,ny))
                    square[nx][ny]= 1
    return cnt

num_input = input().split(" ")
m,n,k = [int(j) for j in num_input]
square = [[0] * n for i in range(m)]

for i in range(k):
    sq = input().split(" ")
    lx,ly,rx,ry = [int(j) for j  in sq]
    ly, ry = m-ry,m-ly
    for x in range(lx,rx):
        for y in range(ly,ry):
            square[y][x] = 1
cnt = 0
ans = []
for i in range(m):
    for j in range(n):
        if square[i][j] == 0:
            ans.append(check_wide(square,cnt+1,i,j))
print(len(ans))
ans_str = ""
ans = sorted(ans)
for i in range(len(ans)):
    if i == len(ans)-1:
        ans_str += str(ans[i])
        break
    else:
        ans_str = ans_str + str(ans[i])
    ans_str += " "
print(ans_str)
