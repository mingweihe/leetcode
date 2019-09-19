import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
            this algorithm would be basic operations for any other puzzles
            so it's good to memorize both of the two solutions
        """
        # Approach 2 time O(n*log(n))
        dp = []
        for x in nums:
            index = bisect.bisect_left(dp, x)
            if index == len(dp):
                dp.append(x)
            else:
                dp[index] = x
        return len(dp)

        # Approach 1 time O(n^2)
        # res = 0
        # dp = [1]*(len(nums))
        # for i in xrange(len(nums)):
        #     for j in xrange(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
        #     res = max(res, dp[i])
        # return res
