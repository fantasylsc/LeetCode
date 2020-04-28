'''

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''


# Hash O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            # only start from new segment
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak        
        
        
# Brute force O(n^3)

# class Solution:
#     def longestConsecutive(self, nums):
#         longest_streak = 0

#         for num in nums: # O(n)
#             current_num = num
#             current_streak = 1

#             while current_num + 1 in nums: # while O(n), lookup O(n)
#                 current_num += 1
#                 current_streak += 1

#             longest_streak = max(longest_streak, current_streak)

#         return longest_streak




# Sort O(nlogn)
        
# class Solution:
#     def longestConsecutive(self, nums):
#         if not nums:
#             return 0

#         nums.sort()

#         longest_streak = 1
#         current_streak = 1

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i-1]:
#                 if nums[i] == nums[i-1]+1:
#                     current_streak += 1
#                 else:
#                     longest_streak = max(longest_streak, current_streak)
#                     current_streak = 1

#         return max(longest_streak, current_streak)        
        
        
        
    

