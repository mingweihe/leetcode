class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        valid = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        s = str(N)
        rs = s[::-1]
        res = ''
        for c in rs:
            if c not in valid: return False
            res += valid[c]
        return res != s
