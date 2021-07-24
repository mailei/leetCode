
class Solution:
    def isPalindrome(self, x: int) -> bool:
        mozi = str(x)
        if x < 0:
            return False       
        if mozi != mozi[::-1]:
            return False
        
        if -2 ** 31 > x or x > 2 ** 31:
            return False
        
        return True
            
            
        
