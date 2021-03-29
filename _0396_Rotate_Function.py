class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = sum(nums)
        cur =  sum(i*x for i, x in enumerate(nums))
        print cur
        ans, n = cur, len(nums)
        for i in xrange(n-1, 0, -1):
            cur =  cur + summ - n * nums[i]
            ans = max(ans, cur)
        return ans
