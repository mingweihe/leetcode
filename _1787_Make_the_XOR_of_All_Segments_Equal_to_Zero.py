from collections import defaultdict


class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnts = [defaultdict(int) for _ in xrange(k)]
        for i, x in enumerate(nums):
            cnts[i%k][x] += 1

        keys, total_nums_cnts = [], []
        for i in xrange(k):
            total_nums_cnts += sum(cnts[i].values()),
            keys += cnts[i].keys(),
        
        dp = [[float('inf')] * 1024 for _ in xrange(k)]
        for i in xrange(1024):
            dp[0][i] = total_nums_cnts[0] - cnts[0][i]
        
        # ith index of the window
        for i in xrange(1, k):
            # base cost of changing current all numbers
            cost_change_all = total_nums_cnts[i] + min(dp[i-1])
            # j represents the number of current xor result
            for j in xrange(1024):
                best = cost_change_all
                # change single number to optimize the base cost of j
                for p in keys[i]:
                    best = min(best, dp[i-1][p ^ j] + total_nums_cnts[i] - cnts[i][p])
                dp[i][j] = best
        return dp[k-1][0]
