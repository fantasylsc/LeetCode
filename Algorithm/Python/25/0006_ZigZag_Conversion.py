'''

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

'''

# https://zhuanlan.zhihu.com/p/30181688

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: # check numRows
            return s
        
        res =  ''
        size = 2 * numRows - 2
        n = len(s)
        i = 0
        
        while i < numRows: # scan from each row
            j = i
            while j < n:
                res += s[j] # append letter in vertical line
                pos = j - i + (size - i) # j - i is the first letter in each V section, size - i is the relative position in this V section
                if i!= 0 and i != numRows - 1 and pos < n:
                    res += s[pos] # add letter not in vertical line
                j += size # increase to next vertical position of this row 
                
            i += 1 # increase row num
            
        return res




