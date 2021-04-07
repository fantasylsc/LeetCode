from collections import Counter


def longestSubstring(s: str, k: int) -> int:
    counter = Counter(s)
    unique_char = len(counter)
    res = 0

    for currUnique in range(1, unique_char + 1):
        char_counter = [0] * 26
        start = 0
        end = 0
        unique = 0
        countAtLeastK = 0
        index = 0

        while end < len(s):
            if unique <= currUnique:
                index = ord(s[end]) - ord('a')
                if char_counter[index] == 0:
                    unique += 1
                char_counter[index] += 1
                if char_counter[index] == k:
                    countAtLeastK += 1
                end += 1
            else:
                index = ord(s[start]) - ord('a')
                if char_counter[index] == k:
                    countAtLeastK -= 1
                char_counter[index] -= 1
                if char_counter[index] == 0:
                    unique -= 1
                start += 1

            if unique == currUnique and unique == countAtLeastK:
                res = max(res, end - start)

    return res

# version2

from collections import Counter
#
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         counter = Counter(s)
#         unique_char = len(counter)
#         res = 0
#
#         for required_unique in range(1, unique_char + 1):
#             freq = {}
#             start = 0
#             end = 0
#             formed_k = 0
#
#             while end < len(s):
#                 if len(freq) <= required_unique:
#                     if s[end] in freq:
#                         freq[s[end]] += 1
#                     else:
#                         freq[s[end]] = 1
#
#                     if freq[s[end]] == k:
#                         formed_k += 1
#
#                     end += 1
#                 else:
#                     if freq[s[start]] == k:
#                         formed_k -= 1
#
#                     freq[s[start]] -= 1
#                     if freq[s[start]] == 0:
#                         del freq[s[start]]
#
#                     start += 1
#
#                 if len(freq) == required_unique and len(freq) == formed_k:
#                     res = max(res, end - start)
#
#         return res



