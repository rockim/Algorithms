fibmemo=[[1,0],[0,1]]
def fibonacci(n):
    global fibmemo
    if len(fibmemo)<=n:
        fibonacci(n-1)
        fibonacci(n-2)
        fibmemo.append([fibmemo[n-1][0]+fibmemo[n-2][0],fibmemo[n-1][1]+fibmemo[n-2][1]])
    else:
        return
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        num = int(input())
        fibonacci(num)
        print(fibmemo[num][0],fibmemo[num][1])