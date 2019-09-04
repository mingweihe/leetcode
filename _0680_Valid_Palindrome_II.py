class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        abca
        azbzza
        note: isPalindrome would check subinterval instead of a new string.
        """
        # Approach 2
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                l = s[i:j]
                r = s[i + 1:j + 1]
                return l == l[::-1] or r == r[::-1]
            else:
                i, j = i + 1, j - 1
        return True
        # Approach 1
        # def isPalindrome(s, l, r):
        #     while l<r:
        #         if s[l] != s[r]: return False
        #         l,r= l+1,r-1
        #     return True
        #
        # i,j = 0,len(s)-1
        # while i < j:
        #     if s[i] != s[j]:
        #         return isPalindrome(s,i,j-1) or isPalindrome(s,i+1,j)
        #     i,j=i+1,j-1
        # return True
