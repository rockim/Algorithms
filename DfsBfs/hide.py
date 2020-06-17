from collections import deque

def bfs():
    while q:
        temp =q.popleft()
        if temp == k:
            return bush[temp]
        next(temp-1,temp)
        next(temp+1,temp)
        next(temp*2,temp)

def next(nex,cur):
    if 0<= nex < 100001 and (bush[nex]==0 or bush[cur]+1 < bush[nex]):
        bush[nex] = bush[cur] + 1
        q.append(nex)
        
            
         
if __name__ == "__main__":
    a = input().split(" ")
    n,k = [int(i) for i in a]
    bush = [0] * 100001
    q = deque([n])
    
    print(bfs())