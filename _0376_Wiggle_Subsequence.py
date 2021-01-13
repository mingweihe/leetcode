class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Approach 3
        if not nums: return 0
        inc = dec = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc = dec + 1
            elif nums[i] < nums[i-1]:
                dec = inc + 1
        return max(inc, dec)
        
        ## Approach 2
        # if not nums: return 0
        # diff = []
        # for i in xrange(1, len(nums)):
        #     if nums[i] == nums[i-1]: continue
        #     diff += nums[i] - nums[i-1],
        # if not diff: return 1
        # res = 2
        # for i in xrange(1, len(diff)):
        #     if diff[i] * diff[i-1] < 0:
        #         res += 1
        # return res
    
        ## Approach 1
        # dp = []
        # for x in nums:
        #     if not dp:
        #         dp += x,
        #         continue
        #     if x == dp[-1]:
        #         continue
        #     if len(dp) == 1:
        #         dp += x,
        #         continue
        #     if dp[-1] > dp[-2]:
        #         if x > dp[-1]: dp[-1] = x
        #         else: dp += x,
        #     else:
        #         if x < dp[-1]: dp[-1] = x
        #         else: dp += x,
        # return len(dp)
