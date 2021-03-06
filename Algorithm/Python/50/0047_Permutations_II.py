'''

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]



'''

# pay attention to skip condition
# sort nums
# compare with permutations I

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        used = [0] * n
        current = []
        
        def dfs():
            if len(current) == n:
                ans.append(current[:])
                return
            # if nums[i] is used, skip
            for i in range(n):
                if used[i]:
                    continue
                # same number can only be used once at each depth
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = 1
                current.append(nums[i])
                dfs()
                current.pop()
                used[i] = 0
            
        dfs()
        return ans
                
'''
[1,2,2]

      [1]                   [2]                [2] X
 [1,2]   [1,2] X       [2,1]   [2,2]      
[1,2,2]              [2,1,2]  [2,2,1]  

'''
        

# backtrack with checking duplicates and pruning

# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         self.nums = nums
#         self.res = []
#         self.backtrack(0)
#         return self.res
        
#     def backtrack(self, start):
#         if start == len(self.nums):
#             if self.nums[:] not in self.res:
#                 self.res.append(self.nums[:])
#             return
#         for i in range(start, len(self.nums)):
              # can only prevent duplication when nums[start] == nums[i]
#             if i != start and self.nums[start] == self.nums[i]: # pruning
#                 continue
#             self.nums[start], self.nums[i] = self.nums[i], self.nums[start]
#             self.backtrack(start + 1)
#             self.nums[start], self.nums[i] = self.nums[i], self.nums[start]

# approach 3

# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         visited = [0] * len(nums)
#         out = []
#         nums.sort()
#         self.permuteDFS(nums, 0, visited, out, res)
#         return res
        
#     def permuteDFS(self, nums, level, visited, out, res):
#         if level >= len(nums):
#             res.append(out[:])
#             return
#         for i in range(len(nums)):
#             if visited[i] == 1: # nums[i] was appended before, skip
#                 continue
#             if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
#                 continue
#             visited[i] = 1
#             out.append(nums[i])
#             self.permuteDFS(nums, level + 1, visited, out, res)
#             out.pop()
#             visited[i] = 0




