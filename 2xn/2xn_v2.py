import math

def combination(n,r):
    n_f = math.factorial(n)
    r_f = math.factorial(r)
    nr_f = math.factorial(n-r)
    return n_f//(r_f * nr_f)

if __name__ == "__main__":
    a = int(input())
    if( a>0):
        div2 = a//2+1
    else:
        div2 = 0
    count = 0
    for i in range(div2):
        d1 = a-i*2
        if i==0:
            count+=1
        elif d1 == 0:
            count += 2**i
        else:
            n = i + d1
            count += (2**i)*combination(n,i)
    answer = count % 10007
    print(answer)

