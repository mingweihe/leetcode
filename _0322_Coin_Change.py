class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Approach 2 dynamic programming
        dp = [0] + [float('inf')] * (amount)
        for i in xrange(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount] == float('inf') else dp[amount]

        # Approach 1 dfs + pruning
        # coins.sort(reverse=True)
        # res = [float('inf')]
        #
        # def dfs(idx, remain, cnt):
        #     if idx == len(coins) - 1:
        #         if remain % coins[idx] == 0:
        #             res[0] = min(res[0], cnt + remain / coins[idx])
        #         return
        #     for k in xrange(remain / coins[idx], -1, -1):
        #         if cnt + k > res[0]: return
        #         dfs(idx + 1, remain - coins[idx] * k, cnt + k)
        #
        # dfs(0, amount, 0)
        # return -1 if res[0] == float('inf') else res[0]
