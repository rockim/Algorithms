memo = [100]
def find(num,count):
    global memo
    if(memo[0]<=count):
        return memo[0]
    if(num==1):
        memo[0] = Min(memo[0],count)
        return memo[0]
    if(num%3 == 0 and num%2 == 0):
        return find(num/3,count+1)
    elif(num%3 == 0 and num%2 != 0):
        return Min(find(num/3,count+1),find(num-1,count+1))
    elif(num%2 == 0 and num%3 != 0):
        return Min(find(num/2,count+1),find(num-1,count+1))
    else:
        return find(num-1,count+1)
def Min(a,b):
    if a>=b:
        return b
    else:
        return a
    
if __name__ == '__main__':
    n = int(input())
    print(find(n,0))

