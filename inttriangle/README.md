# Problem
Given N, give a triangle of integers of size N, as shown below:

'
        7
        
       3  8
       
      8  1  0
      
     2  7  4  4
     
    4  5  2  6  5'

Starting at the top floor and going downstairs by choosing one of the numbers below, make program that print maximum sum of choosen numbers. the number on the downstair can only be selected from the diagonal left or diagonal right of the selected number on the current stair.

# Input
First line is N(1<=N<=500), from second line to n+1 line given integer triangle.

# Output
print tha maximum sum of selected numbers

# How to solve

I made 2'd array that is int triangle

the above integer triangle in an array :
 
 tri = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]

ex) tri[stair][num]  if stair = 1 num = 0 , 3

Use dynamic programing.

if you choose i'stairs n number, 

dp[i][n] = tri[i][n] + max(dp[i-1][n-1],dp[i-1][n]) ( i is not first number and last number)

