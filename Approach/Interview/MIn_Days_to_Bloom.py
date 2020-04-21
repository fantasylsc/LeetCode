'''

Given an array of roses. roses[i] means rose i will bloom on day roses[i]. Also given an int k, which is the minimum number of 
adjacent bloom roses required for a bouquet, and an int n, which is the number of bouquets we need. Return the earliest day 
that we can get n bouquets of roses.

Example:
Input: roses = [1, 2, 4, 9, 3, 4, 1], k = 2, n = 2
Output: 4
Explanation:
day 1: [b, n, n, n, n, n, b]
The first and the last rose bloom.

day 2: [b, b, n, n, n, n, b]
The second rose blooms. Here the first two bloom roses make a bouquet.

day 3: [b, b, n, n, b, n, b]

day 4: [b, b, b, n, b, b, b]
Here the last three bloom roses make a bouquet, meeting the required n = 2 bouquets of bloom roses. So return day 4.

'''


import unittest
from collections import deque

# dp

class Solution:
    def minDaysBloom(self, roses, k, n):
        '''
        : type roses: list[int]
        : type k : int
        : type n : int
        : rtype : int

        '''
        def fillMax(windowKmax, r, k):
            deq = deque()
            for i in range(len(r)):
                if i >= k and r[i - k] == deq[0]:
                    deq.popleft()
                while deq and r[i] > deq[-1]:
                    deq.pop()
                deq.append(r[i])
                if i >= k - 1:
                    windowKmax[i - k + 1] = deq[0]

        windowKmax = [0] * (len(roses) - k + 1)
        fillMax(windowKmax, roses, k)
        print(windowKmax)
        dp = [[float('inf')] * (len(roses) + 1) for _ in range(n + 1)]
        dp[0] = [0] * (len(roses) + 1)

        for i in range(1, n + 1):
            for j in range(k, len(roses) + 1):
                # dp[i][j] means the min time we need to wait by getting i bouquets from preivous j roses
                # we can get i bouquets from previous j - 1 roses
                # or we can get i - 1 bouquets from previous j - k roses and get 1 bouquets from (j - k, j) roses
                dp[i][j] = min(dp[i][j - 1], max(dp[i - 1][j - k], windowKmax[j - k]))
        print(dp)
        return dp[n][len(roses)]

'''

Test results:
windowKmax = [2, 4, 9, 9, 4, 4]
dp = [[0, 0, 0, 0, 0, 0, 0, 0], [inf, inf, 2, 2, 2, 2, 2, 2], [inf, inf, inf, inf, 9, 9, 4, 4]]

'''

# binary search

# class Solution:
#     def minDaysBloom(self, roses, k, n):
#         '''
#         : type roses: list[int]
#         : type k : int
#         : type n : int
#         : rtype : int

#         '''
#         def fillMax(windowKmax, r, k):
#             deq = deque()
#             for i in range(len(r)):
#                 if i >= k and r[i - k] == deq[0]:
#                     deq.popleft()
#                 while deq and r[i] > deq[-1]:
#                     deq.pop()
#                 deq.append(r[i])
#                 if i >= k - 1:
#                     windowKmax[i - k + 1] = deq[0]
        
#         # n <= 0 means answer <= day, then move search interval left 
#         def search(windowKmax, n, k, day):
#             i = 0
#             while i < len(windowKmax):
#                 if day >= windowKmax[i]:
#                     n -= 1
#                     i += k
#                 else:
#                     i += 1
#             return n <= 0

#         r_min = float('inf')
#         r_max = -1
#         for r in roses:
#             r_max = max(r_max, r)
#             r_min = min(r_min, r)

#         windowKmax = [0] * (len(roses) - k + 1)
#         fillMax(windowKmax, roses, k)
        
#         s = r_min
#         e = r_max
#         while s < e:
#             mid = s + (e - s)//2
#             if search(windowKmax, n, k, mid):
#                 e = mid
#             else:
#                 s = mid + 1
#         return e


'''
    1.union-find is not a good solution, both for code complexity and time complexity are not competitive. if u doubt, show me the code
    2.binary search wrote code more, time complexity is O (L * log(max-min) )
    3.dp wrote little code, time complexity is O(n*L), dp[i][j] means the min time we need to wait by preivous j roses to get i bouquets
    4.both depend on calculate max window in O(n) algorithm https://leetcode.com/problems/sliding-window-maximum/
    5.bottom have follow up.

Java code 

//DP
    int minDaysBloomByDp(int[] roses, int k, int n) {
        int[] windowKmax = new int[roses.length - k + 1];
        fillMax(windowKmax,roses,k);
        int[][] dp = new int[n+1][roses.length + 1];

        for (int i = 1; i <= n; i++) {
            Arrays.fill(dp[i],Integer.MAX_VALUE);
            for (int j = k; j <= roses.length; j++) {
                dp[i][j] = Math.min(dp[i][j - 1], Math.max(dp[i - 1][j - k],windowKmax[j - k]));
            }
        }
        return dp[n][roses.length];
    }

    // get maximum in interval k
    void fillMax(int[] windowKmax, int[] r, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < r.length; i++) {
            if (i >= k && r[i - k] == dq.peekFirst()) dq.pollFirst();
            while (!dq.isEmpty() && r[i] > dq.peekLast()) dq.pollLast();
            dq.offerLast(r[i]);
            if (i >= k - 1) windowKmax[i - k + 1] = dq.peekFirst();
        }
    }

//BS    
    int minDaysBloomByBS(int[] roses, int k, int n) {
        int min = Integer.MAX_VALUE, max = -1;
        for (int r : roses) {
            max = Math.max(r,max);
            min = Math.min(r,min);
        }
        int[] windowKmax = new int[roses.length - k + 1];
        fillMax(windowKmax,roses,k);
        int s = min, e = max;
        while (s <= e) {
            int mid = (e - s)/2 + s;
            if (search(windowKmax,n,k,mid)) {
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }
        return e + 1;
    }
    
    boolean search(int[] win,int n,int k,int day) {
        for (int i = 0; i < win.length; ) {
            if (day >= win[i]) {
                n--;
                i+=k;
            } else {
                i++;
            }
        }
        return n <= 0;
    }

    
5.follow up : could u do it better, if n*k nearly equal to L
time complexity O(n * (L - n * k))

    int minDaysBloomByDp(int[] roses, int k, int n) {
        int[] windowKmax = new int[roses.length - k + 1];
        fillmax(windowKmax,roses,k);
        int[][] dp = new int[n+1][roses.length + 1];
        int fix = n*k;
        for (int i = 1; i <= n; i++) {
            Arrays.fill(dp[i],Integer.MAX_VALUE);
            int st = i * k;
            for (int j = st; j <= roses.length - fix + st; j++) {
                dp[i][j] = Math.min(dp[i][j - 1], Math.max(dp[i - 1][j - k],windowKmax[j - k]));
            }
        }
        return dp[n][roses.length];
    }


'''


class Test(unittest.TestCase):
    def test1(self):
        roses = [1, 2, 4, 9, 3, 4, 1]
        k = 2
        n = 2
        expected = 4
        sol = Solution()
        actual = sol.minDaysBloom(roses, k, n)
        self.assertEqual(actual, expected)
    # def test2(self):
    #     A = "abaa,aadvsbc,bdsdsdb"
    #     B = "aaa,aa"
    #     expected = [2, 0]
    #     sol = Solution()
    #     actual = sol.compareString(A, B)
    #     self.assertEqual(actual, expected)

unittest.main(verbosity = 2)

