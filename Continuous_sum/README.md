# Problem
Find the most big number that is continuous sum of numbers
ex) 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 
answer is 12+21=33

# Input
First line's input is  n(1<= n <= 100,000) and second line input is sequencethat is n number of integer. The Integer of sequence is bigger that -1001 and smaller than 1001

# Output
First line is answer

# How to solve
if you use every case of continous sum, the alog's is very slow when n is 100,000
So I try to use new algorithm that find out how many negative numbers are in the sequence, and if the sum of the sequence on the right is less than zero, return 0.

# runtime error
My code has a runtime error and I can't find where is the error 

problem : <https://www.acmicpc.net/problem/1912>

