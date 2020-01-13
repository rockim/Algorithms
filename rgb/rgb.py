def min(a,b):
    if(a>b): return b
    else: return a
if __name__ == "__main__":
    a = int(input())
    rgb = []
    for i in range(a):
        rgb.append(list(map(int,input().split(' '))))
    dp = [[0]*3 for i in range(a)]
    dp[0] = rgb[0]
    for idx in range(1,a):
        dp[idx][0] = min(dp[idx-1][1],dp[idx-1][2])+rgb[idx][0]
        dp[idx][1] = min(dp[idx-1][0],dp[idx-1][2])+rgb[idx][1]
        dp[idx][2] = min(dp[idx-1][0],dp[idx-1][1])+rgb[idx][2]
    answer = min(min(dp[a-1][0],dp[a-1][1]),dp[a-1][2])
    print(answer)