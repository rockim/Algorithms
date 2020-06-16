a = int(input())
b = a//5
box = 0
for i in range(b,-1,-1):
    
    c = a-(5*i)
    if c%3==0:
        temp = i + c//3
        break
    else:
        temp = -1
print(temp)

