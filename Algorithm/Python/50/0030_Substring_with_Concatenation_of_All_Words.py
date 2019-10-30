
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

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []
        wordCnt = {}
        for i in range(len(words)):
            if words[i] in wordCnt:
                wordCnt[words[i]] += 1
            else:
                wordCnt[words[i]] = 1

        
        word_len = len(words[0])
        n = len(words)
        res = []
        
        for i in range(len(s) - n * word_len + 1):
            strCnt = {}
            j = 0
            while j < n:
                t = s[i + j * word_len: i + j * word_len + word_len]
                if t not in wordCnt: # t not in words
                    break
                if t not in strCnt:
                    strCnt[t] = 1
                else:
                    strCnt[t] += 1
                if strCnt[t] > wordCnt[t]: # strCnt doesn't match wordCnt
                    break
                j += 1
            if j == n:
                res.append(i)
                
        return res
        



