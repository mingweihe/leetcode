class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## Approach 2
        nums.sort()
        dp = [[x] for x in nums]
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)
    
        ## Approach 1
        # d = {-1: []}
        # nums.sort()
        # for x in nums:
        #     d[x] = max([v for k, v in d.items() if x % k == 0], key=len) + [x]
        # return max(d.values(), key=len)
