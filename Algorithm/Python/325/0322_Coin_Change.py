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

# Recursion with memorization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        self.count = [0] * amount
        return self.helper(coins, amount)
        
    def helper(self, coins, rem):
        # Base case
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        
        # Memorization
        if self.count[rem - 1] != 0:
            return self.count[rem - 1]
        
        # for each coin in coins, update optimal minimum value
        min_value = float('inf')
        for coin in coins:
            temp = self.helper(coins, rem - coin)
            if temp >= 0 and temp < min_value:
                min_value = temp + 1
                
        if min_value == float('inf'): # no update means cannot be made up by any combination of the coins
            self.count[rem - 1] = -1
        else:
            self.count[rem - 1] = min_value # update with min_value
        return self.count[rem - 1]





