#https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        if s == "":
            return 0
        
        string = ""
        count = 0
        if s[0] == "-" or s[0] == "+":
            string = s[0]
            s = s[1:]
            
        try:
            while s[count].isdigit():
                string += s[count]
                count += 1
        except:
            pass
        
        try:
            string = int(string)
        except:
            return 0
        
        if string > (2**31-1):
            return 2**31-1
        if string < ((-2)**31):
            return ((-2)**31)
        
        return string