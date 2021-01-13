class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
            sweep line algorithm
        """
        n = len(nums)
        cnts = [0] * (n+1)
        for s, e in requests:
            cnts[s] += 1
            cnts[e+1] -= 1
        for i in xrange(1, n+1):
            cnts[i] += cnts[i-1]
        res = 0
        for c, v in zip(sorted(cnts[:-1]), sorted(nums)):
            res += c * v
        return res % (10**9+7)
