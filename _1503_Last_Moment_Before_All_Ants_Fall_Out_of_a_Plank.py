class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        left_end = max(left or [0])
        right_end = min(right or [n])
        return max(left_end, n-right_end)
