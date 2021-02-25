
'''

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        
        if n == 0:
            return 0
        if m < n:
            return -1
        
        for i in range(0, m - n + 1):
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    break
                if j == n - 1:
                    return i
        return -1

# Rabin Carp

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         L, n = len(needle), len(haystack)
#         if L > n:
#             return -1
#
#         # base value for the rolling hash function
#         a = 26
#         # modulus value for the rolling hash function to avoid overflow
#         modulus = 2 ** 31
#
#         # lambda-function to convert character to integer
#         h_to_int = lambda i: ord(haystack[i]) - ord('a')
#         needle_to_int = lambda i: ord(needle[i]) - ord('a')
#
#         # compute the hash of strings haystack[:L], needle[:L]
#         h = ref_h = 0
#         for i in range(L):
#             h = (h * a + h_to_int(i)) % modulus
#             ref_h = (ref_h * a + needle_to_int(i)) % modulus
#         if h == ref_h:
#             return 0
#
#         # const value to be used often : a**L % modulus
#         aL = pow(a, L, modulus)
#         for start in range(1, n - L + 1):
#             # compute rolling hash in O(1) time
#             h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
#             if h == ref_h:
#                 return start
#
#         return -1






