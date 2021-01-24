class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans = 0
        cur = 0
        for x in gain:
            cur += x
            ans = max(ans, cur)
        return ans
