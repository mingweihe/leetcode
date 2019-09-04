class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        dynamic programming / greedy method
        """
        # Approach 3
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 2], cost[i - 1])
        return min(cost[-1], cost[-2])
        # Approach 2
        # p1, p2 = cost[0], cost[1]
        # for item in cost[2:]:
        #     p1, p2 = p2, min(p1, p2) + item
        # return min(p1, p2)
        # Approach 1
        # p1, p2 = cost[0], cost[1]
        # for item in cost[2:]:
        #     t = p1
        #     p1 = p2
        #     p2 = min(t, p2) + item
        # return min(p1, p2)
