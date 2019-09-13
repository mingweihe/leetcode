class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {'6':'9', '8':'8', '9':'6', '1':'1', '0':'0'}
        l, r = 0, len(num)-1
        while l <= r:
            if num[l] not in d: return False
            elif d[num[l]] != num[r]: return False
            l += 1
            r -= 1
        return True
