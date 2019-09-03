class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, l = 0, len(s)
        for i in range(l):
            res += (ord(s[i])-64)*pow(26, l-i-1)
        return res
