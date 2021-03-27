
'''

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

'''


# Extention of problem strStr

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []

        res = []
        m = len(words)
        n = len(words[0])
        wordCounter = Counter(words)

        for i in range(len(s) - m * n + 1):
            k = m
            j = i
            copy = wordCounter.copy()

            while k > 0:
                sub_string = s[j: j + n]

                if sub_string not in copy or copy[sub_string] < 1:
                    break

                copy[sub_string] -= 1
                k -= 1
                j += n

            if k == 0:
                res.append(i)

        return res
        



