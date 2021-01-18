class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
            sometimes dp can be started from the brute force solution
        """
        ## Approach 4, 1D DP
        summ = sum(nums)
        if summ & 1: return False
        half = summ >> 1
        dp = [True] + [False] * half
        for x in nums:
            for t in xrange(half, x-1, -1):
                dp[t] = dp[t] or dp[t-x]
            if dp[-1]: return True
        return False
        
        ## Approach 3, 2D DP
        # summ = sum(nums)
        # if summ & 1: return False
        # half = summ >> 1
        # dp = [[False] * (half + 1) for _ in xrange(len(nums)+1)]
        # for i in xrange(1, len(nums)+1):
        #     for j in xrange(1, half+1):
        #         if j-nums[i-1] == 0:
        #             dp[i][j] = True
        #             continue
        #         elif j-nums[i-1] > 0:
        #             dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        # return dp[-1][-1]
        
        ## Approach 2, hashset
        # summ = sum(nums)
        # if summ & 1: return False
        # half = summ >> 1
        # sums = {0}
        # for u in nums:
        #     _set = []
        #     for v in sums:
        #         _sum = u + v
        #         if _sum == half: return True
        #         if _sum > half or _sum in sums: continue
        #         _set += _sum,
        #     sums.update(_set)
        # return False
    
        ## Approach 1, O(n!) TLE
        # def dfs(cur):
        #     if cur == half: return True
        #     if cur > half: return False
        #     for i in xrange(len(nums)):
        #         if i in seen: continue
        #         seen.add(i)
        #         if dfs(cur + nums[i]): return True
        #         seen.discard(i)
        #     return False
        # summ = sum(nums)
        
        # if summ & 1: return False
        # half = summ >> 1
        # seen = set()
        # return dfs(0)
