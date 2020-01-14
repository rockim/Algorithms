a= int(input())
if (a<2):
    print(1)
else:
    dp = [0 for i in range(a)]  
    dp[0] = 1
    dp[1] = 1
    for i in range(2,a):
        dp[i] = dp[i-2]+dp[i-1]
    print(dp[a-1])