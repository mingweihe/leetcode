class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res = 0
        for x in arr1:
            ok = 1
            for y in arr2:
                ok &= abs(x-y) > d
                if not ok: break
            res += ok
        return res
