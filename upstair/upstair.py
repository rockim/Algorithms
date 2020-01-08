stair_p = [0]
def upstair(n,count):
    global stair_p
    count1 = count+1
    if(n >= len(stair_p)):
        return 0
    score = stair_p[n]
    if(n == len(stair_p)-1):
        return score
    else:
        if(count != 2):
            score += max(upstair(n+1,count1),upstair(n+2,1))
            return score
        else:
            score += upstair(n+2,1)
            return score
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        stair_p.append(int(input()))
    print(upstair(0,0))
    
    
