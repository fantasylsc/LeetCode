
'''

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates 

where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.DFS(candidates, target, 0, [])
        return self.res 
        
        
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            self.res.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]]) 
        
# backtrack
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         self.res = []
#         curr = []
#         self.helper(candidates, target, curr, 0)
#         return self.res
        
#     def helper(self, candidates, target, curr, start):
#         Curr_sum = sum(curr)
#         if Curr_sum > target:
#             return
        
#         if Curr_sum == target:
#             self.res.append(curr[:])
#             return
        
#         for i in range(start, len(candidates)):
#             curr.append(candidates[i])
#             self.helper(candidates, target, curr, i)
#             curr.pop()


