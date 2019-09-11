class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        def helper(lo, hi):
            cur_max = last_second = last_one = 0
            for i in xrange(lo, hi+1):
                cur_max = max(nums[i]+last_second, last_one)
                last_second = last_one
                last_one = cur_max
            return cur_max
        return max(helper(0, len(nums)-2), helper(1, len(nums)-1))
