'''

Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

 

Note:

    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
        
        
# Reverse string, then reverse each word

# class Solution:
#     def trim_spaces(self, s: str) -> list:
#         left, right = 0, len(s) - 1
#         # remove leading spaces
#         while left <= right and s[left] == ' ':
#             left += 1
        
#         # remove trailing spaces
#         while left <= right and s[right] == ' ':
#             right -= 1
        
#         # reduce multiple spaces to single one
#         output = []
#         while left <= right:
#             if s[left] != ' ':
#                 output.append(s[left])
#             elif output[-1] != ' ':
#                 output.append(s[left])
#             left += 1
        
#         return output
            
#     def reverse(self, l: list, left: int, right: int) -> None:
#         while left < right:
#             l[left], l[right] = l[right], l[left]
#             left, right = left + 1, right - 1
            
#     def reverse_each_word(self, l: list) -> None:
#         n = len(l)
#         start = end = 0
        
#         while start < n:
#             # go to the end of the word
#             while end < n and l[end] != ' ':
#                 end += 1
#             # reverse the word
#             self.reverse(l, start, end - 1)
#             # move to the next word
#             start = end + 1
#             end += 1
                
#     def reverseWords(self, s: str) -> str:
#         # converst string to char array 
#         # and trim spaces at the same time
#         l = self.trim_spaces(s)
        
#         # reverse the whole string
#         self.reverse(l, 0, len(l) - 1)
        
#         # reverse each word
#         self.reverse_each_word(l)

# Deque

# from collections import deque
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         left, right = 0, len(s) - 1
#         # remove leading spaces
#         while left <= right and s[left] == ' ':
#             left += 1
        
#         # remove trailing spaces
#         while left <= right and s[right] == ' ':
#             right -= 1
            
#         d, word = deque(), []
#         # push word by word in front of deque
#         while left <= right:
#             if s[left] == ' ' and word:
#                 d.appendleft(''.join(word))
#                 word = []
#             elif s[left] != ' ':
#                 word.append(s[left])
#             left += 1
#         d.appendleft(''.join(word))
        
#         return ' '.join(d)

