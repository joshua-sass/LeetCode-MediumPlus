#https://leetcode.com/problems/multiply-strings/submissions/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        int_num1 = 0
        int_num2 = 0
        
        for iterate in range(0, len(num1)):
            int_num1 += int(num1[iterate]) * 10**(len(num1)- iterate - 1)
            
        for iterate in range(0, len(num2)):
            int_num2 += int(num2[iterate]) * 10**(len(num2)- iterate - 1)
            
        return str(int_num1 * int_num2)