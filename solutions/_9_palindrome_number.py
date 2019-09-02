class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        res=str(x)[::-1]
        if int(res) == x:
            return True
        return False
