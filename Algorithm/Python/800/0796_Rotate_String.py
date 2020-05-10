'''

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

Note:

    A and B will have length at most 100.


'''

# check whether B is a substring of A + A
# check subtring: 1) simple check
#                 2) Rolling Hash

# simple check
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A

        
# Rolling hash
# class Solution:
#     def rotateString(self, A: str, B: str) -> bool:
#         MOD = 10**9 + 7
#         P = 113
#         Pinv = pow(P, MOD-2, MOD)

#         hb = 0
#         power = 1
#         for x in B:
#             code = ord(x) - 96
#             hb = (hb + power * code) % MOD
#             power = power * P % MOD

#         ha = 0
#         power = 1
#         for x in A:
#             code = ord(x) - 96
#             ha = (ha + power * code) % MOD
#             power = power * P % MOD

#         if ha == hb and A == B: return True
#         for i, x in enumerate(A):
#             code = ord(x) - 96
#             ha += power * code
#             ha -= code
#             ha *= Pinv
#             ha %= MOD
#             if ha == hb and A[i+1:] + A[:i+1] == B:
#                 return True
#         return False


# brute force

# class Solution:
#     def rotateString(self, A: str, B: str) -> bool:
#         if len(A) != len(B):
#             return False
#         if len(A) == 0:
#             return True

#         for s in range(len(A)):
#             if all(A[(s+i) % len(A)] == B[i] for i in range(len(A))):
#                 return True
#         return False
