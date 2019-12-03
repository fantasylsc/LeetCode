'''

Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
 

Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.

'''

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # get frequency of the smallest character in a word
        # O(M * N + (M + N) * KlogK), M: len(queries), N: len(words), K: avg length of each word
        def getFrequency(word):
            dic = {}
            for s in word:
                if s in dic:
                    dic[s] += 1
                else:
                    dic[s] = 1
            res = sorted(dic.items())
            return res[0][1]
        
        q = []
        w = []
        result = []
        
        for word in queries:
            q.append(getFrequency(word))
        for word in words:
            w.append(getFrequency(word))
            
        for i in range(len(q)):
            count = 0
            for j in range(len(w)):
                if q[i] < w[j]:
                    count += 1
            result.append(count)
        return result
            

# optimized with binary search

import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # get frequency of the smallest character in a word
        # O(M * logN + + (M + N) * KlogK)
        def getFrequency(word):
            dic = {}
            for s in word:
                if s in dic:
                    dic[s] += 1
                else:
                    dic[s] = 1
            res = sorted(dic.items())
            return res[0][1]
        
        q = []
        w = []
        result = []
        
        for word in queries:
            q.append(getFrequency(word))
        for word in words:
            w.append(getFrequency(word))
        
        w.sort()
        for i in range(len(q)):
            index = bisect.bisect(w, q[i])
            result.append(len(w) - index)
        return result



"""
Note:


1. Counter + Brute Force (TLE)

Time: O(N * M * K^2), M: len(queries), N: len(words), K: avg length of each word
Space: O(M)
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            count = collections.Counter(s)
            return count[min(count.keys())] '''O(K^2)'''
        res = [0] * len(queries)
        for i, query in enumerate(queries):
            for word in words:
                if f(query) < f(word):
                    res[i] += 1
        return res
2. (Optimized) Use Memo to save min char frequency for words and queries

Time: (M * N + (M + N) * KlogK)
Space: O(M + N)
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            t = sorted(list(s))[0] 
            return s.count(t) '''O(KlogK)'''
        memoQ = [f(x) for x in queries]
        memoW = [f(x) for x in words]  '''(M + N) * KlogK'''
        res = []
        for qc in memoQ: '''M * N'''
            count = 0
            for wc in memoW:
                if wc > qc:
                    count+=1
            res.append(count)
        return res
3. Binary Search

Time:
N * (logN + K^2) + M * ( logN + K^2)
==>(N + M) * (logN + K^2)
Space: O(N * K)
what are we binary searching for? - The ceiling of the minimum character frequency of each query

e.g. 'aaab'  --> a:3
      f = [1 2 4 5], len = 4
               ^
             idx = 2

len - idx = 2 --> there are 2 words has min character frequency greater than 'aaab'
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = sorted([w.count(min(w)) for w in words]) '''O(N * K^2 + NlogN)'''
        N = len(f)
        res = []
        for q in queries: '''O(M * (K^2 + logN))'''
            cnt = q.count(min(q))
            idx = bisect.bisect(f, cnt)
            res.append(N - idx)
        return res




"""


