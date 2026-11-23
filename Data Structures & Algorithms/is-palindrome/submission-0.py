class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r: #doing until hits middle
            while l < r and not s[l].isalnum(): #finding next valid alpha num char
                l+=1
            while l < r and not s[r].isalnum(): #finding next valid alpha num char
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True 
                