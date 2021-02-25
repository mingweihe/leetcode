class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        rem = [0] * k
        for x in arr:
            rem[x % k] += 1
        if rem[0] & 1: return False
        if k & 1 == 0 and rem[k/2] & 1: return False
        for i in xrange(1, k / 2 + 1):
            if rem[i] != rem[k-i]: return False
        return True
