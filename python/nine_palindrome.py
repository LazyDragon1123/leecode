class Solution:
    def isPalindrome(self, x:int) -> bool:
        sx = str(x)
        if sx[::-1] == sx:
            return True
        else:
            return False
