n = int(input())
wine = [0]
for i in range(n):
    wine.append(int(input()))

drink_count = 0
dp = [0]*(n+1)
answer=0
if(n<3):
    for ans in wine:
        answer += ans

    print(answer)
else:  
    dp[1] = wine[1]
    dp[2] = wine[1]+wine[2]
    for i in range(3,n+1):
        dp[i] = max(max(dp[i-1],dp[i-2]+wine[i]),dp[i-3]+wine[i-1]+wine[i])
    print(dp[n])
    
