class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
            time complexity: O(32*n)
        """
        res, seen = float('inf'), set()
        for x in arr:
            seen = {x & ss for ss in seen} | {x}
            res = min(res, min(abs(x-target) for x in seen))
        return res
