class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## Approach 2
        dp = [1] + [0] * target
        for i in xrange(1, target + 1):
            for x in nums:
                if i - x >= 0:
                    dp[i] += dp[i-x]
        return dp[-1]
        
        ## Approach 1, memorized recursion
        # def dfs(cur):
        #     if cur == target: return 1
        #     if cur > target: return 0
        #     if cur in cache: return cache[cur]
        #     ans = 0
        #     for x in nums:
        #         ans += dfs(cur + x)
        #     cache[cur] = ans
        #     return ans
        # cache = dict()
        # return dfs(0)
