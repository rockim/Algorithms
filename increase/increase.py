a = int(input())
b = list(map(int,input().split(" ")))

dp = [0 for i in range(a)]       
answer = 0         
for i in range(a):
    if(dp[i] == 0): dp[i] = 1
    for j in range(i):
        if(b[i]>b[j]):
            if(dp[i]<dp[j]+1):
                dp[i] = dp[j]+1
    if( answer < dp[i]):
        answer = dp[i]

print(answer)