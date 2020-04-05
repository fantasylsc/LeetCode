'''

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.


'''

# This approach is much clearer than the second one

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 1. number of words in a line
        # 2. last line or not
        # 3. adjuste each line
        
        res = []
        len_words = len(words)
        i = 0 # start index in a line
        while i < len_words:
            j = i # end index in a line
            cur_len = 0 # count temporal length of a line
            # j - i is the space number 
            # calculate end index of current line
            while j < len_words and cur_len + len(words[j]) + j - i <= maxWidth:
                cur_len += len(words[j])
                j += 1
                
            line = ''
            space = maxWidth - cur_len
            # add ith to jth words and space into current line
            k = i
            while k < j:
                line += words[k]
                if space > 0:
                    if j == len_words: # if this is the last line
                        if j - k == 1: # if this is the last word
                            n_space = space
                        else:
                            n_space = 1
                    else:
                        if (j - 1) - k > 0: # if k is not the last word in this line
                            if space % (j - k - 1) == 0: # if space is divisable
                                n_space = space // (j - k - 1)
                            else:
                                n_space = space // (j - k - 1) + 1
                        else: # k is the last word in this line
                            n_space = space
                    line += ' ' * n_space
                    space -= n_space
                k += 1
            res.append(line)
            i = j
        
        return res
            
# solution 2

# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         res = []
#         row_list = []
#         n = len(words)
#         space = maxWidth
#         char_length = 0
        
#         for i in range(n):
#             print(i)
#             if len(words[i]) <= space: # space can hold new word
#                 row_list.append(words[i])
#                 space = space - (len(words[i]) + 1)
#                 char_length += len(words[i])
#                 if i == n - 1:
#                     row_string = ''
#                     for k in range(len(row_list)):
#                         if k == len(row_list) - 1:
#                             row_string += row_list[k]
#                             row_string += ' ' * (maxWidth - len(row_string))
#                         else:
#                             row_string += row_list[k] + ' '
#                     print(row_string)
#                     res.append(row_string)
#                     print('res:', res)
#                     return res
                
#             else: # process current row_list if space can't hold new word
#                 row_string = ''
#                 if len(row_list) == 1:
#                     n_space = maxWidth - len(row_list[0])
#                     row_string += row_list[0] + ' ' * n_space
#                     print(row_string)
#                     res.append(row_string)
#                 else:
#                     if (maxWidth - char_length) % (len(row_list) - 1) == 0:
#                         n_space = (maxWidth - char_length) // (len(row_list) - 1)
#                         row_string += row_list[0]
#                         for k in range(1, len(row_list)):
#                             row_string += ' ' * n_space + row_list[k]
#                         print(row_string)
#                         res.append(row_string)
#                     else:
#                         n_space1 = (maxWidth - char_length) // (len(row_list) - 1)
#                         n_space2 = (maxWidth - char_length) % (len(row_list) - 1)
#                         row_string += row_list[0]
#                         for k in range(1, len(row_list)):
#                             if n_space2:
#                                 n_space = n_space1 + 1
#                                 n_space2 -= 1
#                                 row_string += ' ' * n_space + row_list[k]
#                             else:
#                                 row_string += ' ' * n_space1 + row_list[k]
#                         print(row_string)
#                         res.append(row_string)
                    
#                 # add new word to row_list after processing row_list
#                 row_list = []
#                 space = maxWidth
#                 char_length = 0
#                 char_length += len(words[i])
#                 row_list.append(words[i])
#                 space = space - (len(words[i]) + 1)
#                 if i == n - 1:
#                     row_string = ''
#                     n_space = maxWidth - char_length
#                     row_string += row_list[0] + ' ' * n_space
#                     print(row_string)
#                     res.append(row_string)
#                     print(res)
#                     return res
                    


