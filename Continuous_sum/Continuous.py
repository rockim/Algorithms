num = []
memostart = []
def con_add(n):
    print(n,"st")
    global num
    numsum = 0
    count = 0
    for i in range(n,len(num)):
        if num[i] < 0 and count != 0:
            numsum = numsum+max(con_add(i),0)
            break
        else:
            numsum = numsum+num[i]
        count += 1
    return numsum
def find_start():
    count = 0
    global memostart, num
    for i in num:
        if  count == 0:
            memostart.append(count)
            if i < 0 and num[count+1] >0:
                memostart.append(count+1)
        elif i < 0 and count<(len(num)-1):
            if(num[count+1]>=0):
                memostart.append(count+1)
        count=count +1

if __name__ == "__main__":
    n = int(input())
    ns = input().split(' ')
    if n == len(ns):
        for i in ns:
            num.append(int(i))
        if len(num)!=1:
            find_start()
            print(memostart)
            answer=-1001
            if(len(memostart)==1 and num[0]<0):
                num.sort()
                answer = num.pop()
            else:
                count = 0
                for i in memostart:
                    if( count == 0):
                        answer = con_add(i)
                    else:
                        answer = max(answer,con_add(i))
                    count+=1
            print(answer)
        else:
            print(num[0])
    else:
        print("error")
