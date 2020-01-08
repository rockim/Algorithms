a = int(input())
st = []
for i in range(a):
    b=int(input())
    st.append(b)
dp = [0]*a

dp[0] = st[0]
dp[1] = max(st[0]+st[1],st[1])
dp[2] = max(st[0]+st[2],st[1]+st[2])

for i in range(3,a):
    dp[i] += max(dp[i-3]+st[i-1]+st[i],dp[i-2]+st[i])

print(dp[a-1])
