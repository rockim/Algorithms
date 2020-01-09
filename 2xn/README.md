# Problem
print number of methos that is Tiling 2xn with 1x2, 2x1 tiles

# Input
first line is n(1 <= n<= 1000)

# Output
print remainder by dividing the number of methods by 10,007.

# Howtosolve

I solve this problem with combination function. Thinking that 2x1 is 1 and 1x2 is 2. I thaught answer is number of methods that represent n by using 1,2. 

ex) 1 is 1 
ex) 2 is 1+1, 2C1(1+2, 2+1)
ex) 3 is 1+1+1, 3C2(2+1+1, 1+2+1, 1+1+2)

problem : <https://www.acmicpc.net/problem/11726>

