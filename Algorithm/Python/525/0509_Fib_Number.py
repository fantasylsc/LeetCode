'''

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.

'''

# Recursion without memoization 1004 ms

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        return self.fib(N - 1) + self.fib(N - 2)


# Recursion with memoization 28 ms

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        self.mem = [float('inf')] * (N + 1)
        self.mem[0] = 0
        self.mem[1] = 1
        
        res = self.helper(N)
        
        return res
    
    def helper(self, N):
        if self.mem[N] != float('inf'):
            return self.mem[N]
        self.mem[N] = self.helper(N - 1) + self.helper(N - 2)
        
        return self.mem[N]

# DP  24 ms

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[N]

