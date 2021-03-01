class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        def dfs(top_i, cost):
            if top_i == m:
                if abs(cost-target) > abs(self.res-target):
                    return
                if abs(cost-target) < abs(self.res-target):
                    self.res = cost
                    return
                self.res = min(self.res, cost)
                return
            dfs(top_i + 1, cost)
            dfs(top_i + 1, cost + toppingCosts[top_i])
            dfs(top_i + 1, cost + toppingCosts[top_i] * 2)
            
        self.res, m = baseCosts[0], len(toppingCosts)
        for b in baseCosts:
            dfs(0, b)
        return self.res
