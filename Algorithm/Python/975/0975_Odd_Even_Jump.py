
'''

You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

    During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
    During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
    (It may be the case that for some index i, there are no legal jumps.)

A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.

 
Example 1:

Input: [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can't jump any more.
From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
From starting index i = 3, we can jump to i = 4, so we've reached the end.
From starting index i = 4, we've reached the end already.
In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some number of jumps.

Note:

    1 <= A.length <= 20000
    0 <= A[i] < 100000

'''

# approach 1, dp + binary search

from sortedcontainers import SortedDict
# there is OrderedDict, it keeps the insertion order but can't sort by itself.

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        m = SortedDict()
        dp = [[0] * 2 for _ in range(n)]
        dp[n - 1][0] = dp[n - 1][1] = 1
        m[A[n - 1]] = n - 1
        res = 1
        
        for i in range(n - 2, -1, -1):
            # return index of lower bound, eg, first item >= A[i]
            # bisect_left return item >= value
            o = m.bisect_left(A[i]) 
            if o != len(m):
                dp[i][0] = dp[m.items()[o][1]][1]
            # index of first item <= A[i]
            # bisect_right return item > val
            # so e - 1 represents item <= val
            e = m.bisect_right(A[i])
            if e != 0:
                dp[i][1] = dp[m.items()[e - 1][1]][0]
            if dp[i][0]:
                res += 1
            m[A[i]] = i
        return res

# class Solution:
#     def oddEvenJumps(self, A: List[int]) -> int:
#         n = len(A)
#         m = SortedDict()
#         dp = [[0] * 2 for _ in range(n)]
#         dp[n - 1][0] = dp[n - 1][1] = 1
#         m[A[n - 1]] = n - 1
#         res = 1
        
#         for i in range(n - 2, -1, -1):
#             # return index of lower bound, eg, first item >= A[i]
#             o = self.lowerBound(m.keys(), A[i])
#             if o != -1:
#                 dp[i][0] = dp[m[o]][1]
#             # index of first item <= A[i]
#             e = self.upperBound(m.keys(), A[i])
#             if e != -1:
#                 dp[i][1] = dp[m[e]][0]
#             if dp[i][0]:
#                 res += 1
#             m[A[i]] = i
#         return res
    
#     def lowerBound(self, nums, target):
#         if target > nums[-1]:
#             return -1
#         if target < nums[0]:
#             return nums[0]
        
#         start = 0
#         end = len(nums) - 1

#         while start + 1 < end:
#             mid = start + (end - start) // 2
#             if nums[mid] == target:
#                 return nums[mid]
#             elif nums[mid] < target:
#                 start = mid
#             else:
#                 end = mid
                
#         if nums[start] == target:
#             return nums[start]
#         if nums[end] == target:
#             return nums[end]

#         return nums[end]
    
#     def upperBound(self, nums, target):
#         if target < nums[0]:
#             return -1
#         if target > nums[-1]:
#             return nums[-1]
        
#         start = 0
#         end = len(nums) - 1

#         while start + 1 < end:
#             mid = start + (end - start) // 2
#             if nums[mid] == target:
#                 return nums[mid]
#             elif nums[mid] < target:
#                 start = mid
#             else:
#                 end = mid
                
#         if nums[start] == target:
#             return nums[start]
#         if nums[end] == target:
#             return nums[end]
        
#         return nums[start]
    
    
    
        

# C++ code

'''
class Solution {
public:
  int oddEvenJumps(vector<int>& A) {
    const int n = A.size();
    map<int, int> m;
    vector<vector<int>> dp(n + 1, vector<int>(2));
    dp[n - 1][0] = dp[n - 1][1] = 1;
    m[A[n - 1]] = n - 1;
    int ans = 1;
    for (int i = n - 2; i >= 0; --i) {
      auto o = m.lower_bound(A[i]);
      if (o != m.end()) dp[i][0] = dp[o->second][1];
      auto e = m.upper_bound(A[i]);
      if (e != m.begin()) dp[i][1] = dp[prev(e)->second][0];
      if (dp[i][0]) ++ans;
      m[A[i]] = i;
    }
    return ans;
  }
};

'''
