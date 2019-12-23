'''

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

'''
# DP

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1        
        

# Optimized DP

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [0] + [float('inf')] * amount
        
#         for coin in coins:
#             for i in range(coin, amount+1):
#                 dp[i] = min(dp[i], dp[i-coin]+1)
        
#         return dp[-1] if dp[-1] != float('inf') else -1  

        
        
# Recursion without return value

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         self.res = float('inf')
#         coins.sort()
#         self.helper(coins, amount, len(coins) - 1, 0)
#         return self.res if self.res != float('inf') else -1
        
#     def helper(self, coins, target, start, curr_res):
#         if target < 0:
#             return
#         if target == 0:
#             self.res = min(self.res, curr_res)
#         for i in range(start, -1, -1):
#             self.helper(coins, target - coins[i], i, curr_res + 1)


# Recusion without memoization

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # Recursion with memorization
#         if amount < 1:
#             return 0
#         # self.count = [0] * amount
#         return self.helper(coins, amount)
        
#     def helper(self, coins, rem):
#         # Base case
#         if rem < 0:
#             return -1
#         if rem == 0:
#             return 0
        
#         # Memorization
#         # if self.count[rem - 1] != 0:
#         #     return self.count[rem - 1]
        
#         # for each coin in coins, update optimal minimum value
#         min_value = float('inf')
#         for coin in coins:
#             temp = self.helper(coins, rem - coin)
#             if temp >= 0 and temp < min_value:
#                 min_value = temp + 1
                
#         if min_value == float('inf'):
#             return -1
#         else:
#             return min_value
#         # if min_value == float('inf'): # no update means cannot be made up by any combination of the coins
#         #     self.count[rem - 1] = -1
#         # else:
#         #     self.count[rem - 1] = min_value # update with min_value
#         # return self.count[rem - 1]

# Recursion with memoization
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount < 1:
#             return 0
#         self.count = [0] * amount
#         return self.helper(coins, amount)
        
#     def helper(self, coins, rem):
#         # Base case
#         if rem < 0:
#             return -1
#         if rem == 0:
#             return 0
        
#         # Memorization
#         if self.count[rem - 1] != 0:
#             return self.count[rem - 1]
        
#         # for each coin in coins, update optimal minimum value
#         min_value = float('inf')
#         for coin in coins:
#             temp = self.helper(coins, rem - coin)
#             if temp >= 0 and temp < min_value:
#                 min_value = temp + 1
                
#         if min_value == float('inf'): # no update means cannot be made up by any combination of the coins
#             self.count[rem - 1] = -1
#         else:
#             self.count[rem - 1] = min_value # update with min_value
#         return self.count[rem - 1]





