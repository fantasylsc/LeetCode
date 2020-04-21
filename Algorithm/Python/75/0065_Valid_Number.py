'''

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

    Numbers 0-9
    Exponent - "e"
    Positive/negative sign - "+"/"-"
    Decimal point - "."

Of course, the context of these characters also matters in the input.


'''

'''
Consider the following cases:
- 空格： 空格可以出现在开头和结尾，不能出现在中间。
- 符号：符号前面如果有字符的话必须是空格或者是自然底数，标记sign为true。
- 数字：标记num和numAfterE为true，numAfterE表示自然底数后面是否有数字。
- 小数点：如果之前出现过小数点或者自然底数，返回false，否则标记dot为true。
- 自然底数：如果之前出现过自然底数或者之前从未出现过数字，返回false，否则标记exp为true，numAfterE为false。
- 其他字符：返回false。

'''

class Solution:
    def isNumber(self, s: str) -> bool:
        num = False
        numAfterE = True
        dot = False
        exp = False
        sign = False
        n = len(s)
        
        for i in range(n):
            if s[i] == ' ':
                if i < n- 1 and s[i + 1] != ' ' and (num or dot or exp or sign):
                    return False
            elif s[i] == '+' or s[i] == '-':
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != ' ':
                    return False
                sign = True
            elif s[i] >= '0' and s[i] <= '9':
                num = True
                numAfterE = True
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            elif s[i] == 'e':
                if exp or not num:
                    return False
                exp = True
                numAfterE = False
            else:
                return False
        return num and numAfterE
        

