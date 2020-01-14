i = int(input())

triangle = []
for s in range(i):
    triangle.append(list(map(int,input().split(" "))))

dp=[[0]*s for s in range(1,i+1)]
dp[0] = triangle[0]
answer = 0
for stair in range(1,i):
    for num in range(stair+1):
        if(num == 0):
            dp[stair][num] = triangle[stair][num] + dp[stair-1][num]
        elif(num==stair):
            dp[stair][num] = triangle[stair][num] + dp[stair-1][num-1]
        else:
            dp[stair][num] = triangle[stair][num] + max(dp[stair-1][num-1],dp[stair-1][num])
for ans in dp[i-1]:
    answer = max(answer,ans)

print(answer)