'''

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

#  DFS, back track
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        used = [0] * n
        current = []
        
        def dfs():
            if len(current) == n:
                ans.append(current[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = 1
                current.append(nums[i])
                dfs()
                current.pop()
                used[i] = 0
        dfs()
        return ans
      
'''

[1,2,3]

[1]                   [2]            [3]
[1,2][1,3]        [2,1][2,3]      [3,1][3,2]
[1,2,3][1,3,2]  [2,1,3][2,3,1]  [3,1,2][3,2,1]

'''

# Back track
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         self.nums = nums
#         self.res = []
#         self.helper(0, n)
#         return self.res
        
#     def helper(self, start, n):
#         if start == n:
#             self.res.append(self.nums[:])
#         for i in range(start, n):
#             self.nums[start], self.nums[i] = self.nums[i], self.nums[start]
#             self.helper(start + 1, n)
#             self.nums[start], self.nums[i] = self.nums[i], self.nums[start]



