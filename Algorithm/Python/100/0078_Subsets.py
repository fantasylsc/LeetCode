'''

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
    
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first = 0, curr = []):
#             # if the combination is done
#             if len(curr) == k:  
#                 output.append(curr[:])
#             for i in range(first, n):
#                 # add nums[i] into the current combination
#                 curr.append(nums[i])
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
        
#         output = []
#         n = len(nums)
#         for k in range(n + 1):
#             backtrack()
#         return output
    
    
    
