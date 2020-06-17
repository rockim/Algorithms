from collections import deque


def bfs(start,n,m,maze):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    dist = [[0]* m for i in range(n)]
    q.append(start)
    dist[0][0] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<= nx < n and 0 <= ny< m:
                if dist[nx][ny] == 0 and maze[nx][ny] == 1:
                    q.append((nx,ny))
                    dist[nx][ny] = dist[x][y] + 1
    return (dist[n-1][m-1])


a= input().split(" ")
N, M = [int(i) for i in a]
maze = []
for i in range(N):
    line = list(map(int,input()))
    maze.append(line)
start = (0,0)

print(bfs(start,N,M,maze))
