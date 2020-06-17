dx = [0,0,-1,1]
dy = [1,-1,0,0]
def dfs(x,y,cnt):
    global ans 
    ans = max(ans, cnt)
    for k in range(4):
        nx,ny = x + dx[k] , y+ dy[k]
        if 0<=nx<R and 0<=ny<C:
            if alpha[board[nx][ny]] == 0:
                alpha[board[nx][ny]] = 1
                dfs(nx,ny,cnt+1)
                alpha[board[nx][ny]] = 0

a = list(map(int,input().split(" ")))
R,C = a[0],a[1]
board = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]
alpha = [0] * 26
ans =1 
alpha[board[0][0]]= 1
dfs(0,0,1)
print(ans)
