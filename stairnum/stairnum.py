a = int(input())

dp = [0,1,1,1,1,1,1,1,1,1]
answer = 0
if(a==1):
    for j in dp:
        answer += j
    print(answer%1000000000)
else:

    for i in range(1,a):
        temp = [0,0,0,0,0,0,0,0,0,0]
        for j in range(10):
            if(j==0):
                temp[0] +=(dp[1])
            elif(j==9):
                temp[9] +=(dp[8])
            else:
                temp[j] += (dp[j-1]+dp[j+1]) 
        dp = temp
                
    for j in dp:
        answer += j
    print(answer%1000000000)
