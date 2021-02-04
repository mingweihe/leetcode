class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prev_subs = 0
        dp = [0]
        for i in xrange(len(arr)):
            if arr[i] & 1: dp += prev_subs - dp[-1] + 1,
            else: dp += dp[-1],
            prev_subs += 1
        return sum(dp) % (10**9 + 7)
