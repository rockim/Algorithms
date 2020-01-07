import math
def add123(n):
    count = 0
    div3 = (n//3)+1
    for  i in range(div3):
        num = n - i*3
        div2 = (num//2)+1
        for j in range(div2):
            div1 = num - j*2
            add = i+j+div1
            if(i > 0):
                if(j>0):
                    count+=combination(add,i)*combination(add-i,j)
                else:
                    count+=combination(add,i)
            else:
                if(j>0):
                    count+=combination(add,j)
                else:
                    count+=1

                    
    return count
def combination(n,r):
    n_f = math.factorial(n)
    r_f = math.factorial(r)
    nr_f = math.factorial(n-r)
    return n_f/(r_f * nr_f)
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        print(int(add123(num)))
