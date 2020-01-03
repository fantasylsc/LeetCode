
'''

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        curr = []
        candidates.sort()
        self.helper(candidates, target, curr, 0)
        return self.res
        
    def helper(self, candidates, target, curr, start):
        Curr_sum = sum(curr)
        if Curr_sum > target:
            return
        
        if Curr_sum == target:
            self.res.append(curr[:])
            return
        
        i = start
        while i < len(candidates):
            curr.append(candidates[i])
            self.helper(candidates, target, curr, i + 1)
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: # generate unique set
                i += 1
            i += 1
        



