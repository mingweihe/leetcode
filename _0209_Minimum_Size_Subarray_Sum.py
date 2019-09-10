import bisect


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Approach 3 bisect right
        res, L = float('inf'), len(nums)
        accum = [0]
        for i in xrange(L):
            accum.append(nums[i]+accum[i])
        for i in xrange(L+1):
            ind = bisect.bisect_right(accum, accum[i]-s)
            if ind != 0: res = min(res, i-ind+1)
        return 0 if res == float('inf') else res

        # Approach 2 bisect left
        # res, L = float('inf'), len(nums)
        # accum = [0]
        # for i in xrange(L):
        #     accum.append(nums[i]+accum[i])
        # for i in xrange(L+1):
        #     ind = bisect.bisect_left(accum, accum[i]+s)
        #     if ind != L+1: res = min(res, ind-i)
        # return 0 if res == float('inf') else res

        # Approach 1
        # res = float('inf')
        # left = summ = 0
        # for i, x in enumerate(nums):
        #     summ += x
        #     while left <= i and summ >= s:
        #         summ -= nums[left]
        #         res = min(res, i-left+1)
        #         left += 1
        # return 0 if res == float('inf') else res
