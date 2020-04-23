'''

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            ans.append(current[:])
            if len(current) == len(nums):
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()
                
        nums.sort()
        ans = []
        current = []
        backtrack(0)
        return ans


# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = [[]]
#         last = None
        
#         for num in nums:
#             if last != num:
#                 last = num
#                 size = len(res)
#             newSize = len(res)
#             for i in range(newSize - size, newSize):
#                 res.append(res[i] + [num])
            
#         return res
        
'''

                        []        
                   /          \        
                  /            \     
                 /              \
              [1]                []
           /       \           /    \
          /         \         /      \        
       [1 2]       [1]       [2]     []
      /     \     /   \     /   \    / \
  [1 2 2] [1 2]  X   [1]  [2 2] [2] X  []


'''




# class Solution:        
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first = 0, curr = []):
#             # if the combination is done
#             # if len(curr) == k:  
#             output.append(curr[:])
#             i = first
#             while i < n:
#                 # add nums[i] into the current combination
#                 curr.append(nums[i])
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
#                 while i + 1 < len(nums) and nums[i] == nums[i + 1]:
#                     i += 1
#                 i += 1
        
#         output = []
#         nums.sort()
#         n = len(nums)
#         # for k in range(n + 1):
#         backtrack()
#         return output        
        
        
        
        



