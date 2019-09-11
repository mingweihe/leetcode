class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Approach 2
        res = []
        if not nums: return res
        i, L = 0, len(nums)
        while i < L:
            num = nums[i]
            while i < L - 1 and nums[i] + 1 == nums[i+1]: i += 1
            if num != nums[i]: res.append(format('%s->%s' % (`num`, `nums[i]`)))
            else: res.append(str(num))
            i += 1
        return res

        # Approach 1
        # if not nums: return []
        # res = []
        # lo, hi = nums[0], nums[0]+1
        # for i in xrange(1, len(nums)):
        #     if nums[i] == hi: hi += 1
        #     else:
        #         if hi == lo + 1: res.append(`lo`)
        #         else: res.append('{}->{}'.format(lo, hi-1))
        #         lo, hi = nums[i], nums[i]+1
        # if hi == lo + 1: res.append(`lo`)
        # else: res.append('{}->{}'.format(lo, hi-1))
        # return res
