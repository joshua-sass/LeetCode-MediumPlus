class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        largest = ""
        for iterator in range(0, len(s)):
            for letter in range(len(largest), len(s)-iterator+1):
                comparison_string = s[iterator:iterator+letter]
                if comparison_string == comparison_string[::-1] and len(comparison_string) > len(largest) :
                    largest = comparison_string
                    
        return largest