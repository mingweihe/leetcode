class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0: return 0
        coins.sort(reverse=True)
        self.result = amount + 1

        def dfs_pruning(coins, remain, index, count, checked=False):
            if not checked:
                p = (remain // coins[index])
                if remain % coins[index] == 0:
                    self.result = min(count + p, self.result)
                    return True
                # pruning
                elif count + p + 1 >= self.result:
                    return False
            if index < len(coins) - 1:
                # take as many large coins as possible
                if coins[index] < remain:
                    dfs_pruning(coins, remain - coins[index], index, count + 1, True)
                dfs_pruning(coins, remain, index + 1, count)

        dfs_pruning(coins, amount, 0, 0)
        return self.result if self.result < amount + 1 else -1
