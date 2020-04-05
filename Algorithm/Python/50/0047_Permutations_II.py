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

# backtrack with checking duplicates

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.backtrack(0)
        return self.res
        
    def backtrack(self, start):
        if start == len(self.nums):
            if self.nums[:] not in self.res:
                self.res.append(self.nums[:])
            return
        for i in range(start, len(self.nums)):
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]
            self.backtrack(start + 1)
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]

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
#             print('put in result:', out[:])
#             res.append(out[:])
#             return
#         for i in range(len(nums)):
#             if visited[i] == 1: # nums[i] was appended before, skip
#                 print('skip 1:', 'i:', i, 'level:', level, 'visited:', visited, out)
#                 continue
#             if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
#                 print('skip 2:', 'i:', i, 'level:', level, 'visited:', visited, out)
#                 continue
#             visited[i] = 1
#             out.append(nums[i])
#             print('append:', 'i:', i, 'level:', level, 'visited:', visited, out)
#             self.permuteDFS(nums, level + 1, visited, out, res)
#             out.pop()
#             visited[i] = 0
#             print('pop:', 'i:', i, 'level:', level, 'visited:', visited, out)

