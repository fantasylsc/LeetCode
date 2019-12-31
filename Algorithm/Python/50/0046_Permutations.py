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

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

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



