class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        cnt, maxi = 0, 0
        res = 0
        for x in light:
            cnt += 1
            maxi = max(maxi, x)
            res += maxi == cnt
        return res
