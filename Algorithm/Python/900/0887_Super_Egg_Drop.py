'''

You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

 

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
 

Note:

1 <= K <= 100
1 <= N <= 10000

'''

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        '''
        
          K ==> Number of eggs
          N ==> Number of floors
          superEggDrop(K, N) ==> Minimum number of trials needed to find the critical
                            floor in worst case.
          superEggDrop(K, N) = 1 + min{max(eggDrop(K - 1, N - 1), eggDrop(K, N - x)): 
                         x in {1, 2, ..., N}}
        
        '''
        # A 2D table where entery eggFloor[i][j] will represent minimum 
        # number of trials needed for i eggs and j floors. 
        eggFloor = [[0] * (N + 1) for _ in range(K + 1)]         
        
        # We need one trial for one floor
        for i in range(1, K + 1):
            eggFloor[i][1] = 1
            
        # We always need j trails for one egg and j floors
        for j in range(1, N + 1):
            eggFloor[1][j] = j
        
        # Fill rest of the table using optimal substructure property
        for i in range(2, K + 1):
            s = 2
            for j in range(2, N + 1):
                eggFloor[i][j] = j
                # eggFloor[i - 1][j - 1] increases with j, it's the same for the optimal point
                while s < j and eggFloor[i - 1][s - 1] < eggFloor[i][j - s]:
                    s += 1
                eggFloor[i][j] = min(eggFloor[i][j], 1 + max(eggFloor[i - 1][s - 1], eggFloor[i][j - s]))
                        
        return eggFloor[K][N]






'''

# Time limit exceeded:

# Dynamic Programming

# O(KN**2)

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """          K ==> Number of eggs
          N ==> Number of floors
          superEggDrop(K, N) ==> Minimum number of trials needed to find the critical
                            floor in worst case.
          superEggDrop(K, N) = 1 + min{max(eggDrop(K - 1, N - 1), eggDrop(K, N - x)): 
                         x in {1, 2, ..., N}}"""
        

        # A 2D table where entery eggFloor[i][j] will represent minimum 
        # number of trials needed for i eggs and j floors. 
        eggFloor = [[0] * (N + 1) for _ in range(K + 1)]         
        
        # We need one trial for one floor
        for i in range(1, K + 1):
            eggFloor[i][1] = 1
            
        # We always need j trails for one egg and j floors
        for j in range(1, N + 1):
            eggFloor[1][j] = j
        
        # Fill rest of the table using optimal substructure property
        for i in range(2, K + 1):
            for j in range(2, N + 1):
                eggFloor[i][j] = j
                for x in range(1, j + 1):
                    res = 1 + max(eggFloor[i - 1][x - 1], eggFloor[i][j - x])
                    if res < eggFloor[i][j]:
                        eggFloor[i][j] = res
                        
        return eggFloor[K][N]
                    

# Time limit exceeded                    
# Dynamic Programming with Binary Search
# O(K NlogN)

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        
          K ==> Number of eggs
          N ==> Number of floors
          superEggDrop(K, N) ==> Minimum number of trials needed to find the critical
                            floor in worst case.
          superEggDrop(K, N) = 1 + min{max(eggDrop(K - 1, N - 1), eggDrop(K, N - x)): 
                         x in {1, 2, ..., N}}
        
        """
        # A 2D table where entery eggFloor[i][j] will represent minimum 
        # number of trials needed for i eggs and j floors. 
        eggFloor = [[0] * (N + 1) for _ in range(K + 1)]         
        
        # We need one trial for one floor
        for i in range(1, K + 1):
            eggFloor[i][1] = 1
            
        # We always need j trails for one egg and j floors
        for j in range(1, N + 1):
            eggFloor[1][j] = j
        
        # Fill rest of the table using optimal substructure property
        for i in range(2, K + 1):
            for j in range(2, N + 1):
                eggFloor[i][j] = j
                left = 1
                right = j
                while left < right:
                    mid = left + (right - left) // 2
                    if eggFloor[i - 1][mid - 1] < eggFloor[i][j - mid]:
                        left = mid + 1
                    else:
                        right = mid
                eggFloor[i][j] = min(eggFloor[i][j], 1 + max(eggFloor[i - 1][right - 1], eggFloor[i][j - right]))
                        
        return eggFloor[K][N]
                    
     

'''
