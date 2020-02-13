# Problem

People who live on RGB streets want to paint their houses in red, green or blue. They also set a rule that all neighbors could not be painted the same color. The house i's neighbors are house i-1 and house i+1


If you are given the cost of painting each house in red, the cost of green, and the cost of bvlue, write a program that calculates the minimum cost of painting all the houses.

# Input

First line, given N that is the number of houses. N is less than or equal to 1,000.


From line 2 to line N, you are charged the cost of painting each house in red, green, and blue. The cost is natural number less than or equal to 1,000.

# Output

Print cost of minimum that painted all houses

# How to solve

Using dynamic programing.

dp = [[0]*3]*a is bad code. --> dp[0] = dp[1] = dp[2] 

So try to dp = [[0]*3 for i in range(a)]

problem : <https://www.acmicpc.net/problem/1149>
