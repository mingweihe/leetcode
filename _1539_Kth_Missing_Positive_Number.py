class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        ss = set(arr)
        for i in xrange(1, arr[-1]+1):
            if i not in ss:
                k -= 1
                if k == 0: return i
        return arr[-1] + k
