'''

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 

Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length


'''

# approach 1 deque
# understand why deq[0] is the largest 
# left item in deque must <= right, else item in left will pop out

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()
                
            # remove from deq indexes of all elements 
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]
        
        # build output
        for i in range(k, n):
            clean_deque(i)          
            deq.append(i)
            output.append(nums[deq[0]])
        return output
        
# approach 2 dp
    
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         if n * k == 0:
#             return []
#         if k == 1:
#             return nums
        
#         left = [0] * n
#         left[0] = nums[0]
#         right = [0] * n
#         right[n - 1] = nums[n - 1]
        
#         for i in range(1, n):
#             # from left to right
#             if i % k == 0:
#                 # block start
#                 left[i] = nums[i]
#             else:
#                 left[i] = max(left[i - 1], nums[i])
#         # for j in range(n - 2, -1, -1):
#         #     if j % k == (k - 1):
#         #         right[j] = nums[j]
#         #     else:
#         #         right[j] = max(right[j + 1], nums[j])
#             from right to left
#             j = n - i - 1
#             if (j + 1) % k == 0:
#                 # block end
#                 right[j] = nums[j]
#             else:
#                 right[j] = max(right[j + 1], nums[j])

#         output = []
#         for i in range(n - k + 1):
#             output.append(max(left[i + k - 1], right[i]))
            
#         return output
        
 
 
# approach 3 naive deque O(nk)

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         q = deque()
#         res = []
        
#         for i in range(k):
#             q.append(nums[i])
#         m = max(q)
#         res.append(m)
        
#         for i in range(k, len(nums)):
#             q.popleft()
#             q.append(nums[i])
#             res.append(max(q))
        
#         return res
            

# approach 4 similar brute force O(nk)
    
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         if n * k == 0:
#             return []
#         return [max(nums[i: i + k]) for i in range(n - k + 1)]
            
        
        
