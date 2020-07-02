'''

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

# backtrack recursion
# for each num in 1...n
# choose or not choose
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        curr = []
        self.helper(n, k, 1, curr)
        return self.res
        
    def helper(self, n, k, start_level, curr):
        if len(curr) == k:
            self.res.append(curr[:])
            return
        for i in range(start_level, n + 1):
            curr.append(i)
            self.helper(n, k, i + 1, curr) # i + 1 (without duplicate) or start_level (with duplicate)
            # if use: self.helper(n, k, start + 1, curr)
            # when i = 2, start = 1, will generate [2, 2]
            curr.pop()
        
