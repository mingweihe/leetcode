class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        res = pre = 0
        for x in target:
            res += max(x-pre, 0)
            pre = x
        return res
