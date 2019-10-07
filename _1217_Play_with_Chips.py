class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        # Approach 2 time O(n)
        even, odd = 0, 0
        for pos in chips:
            if pos & 1: odd += 1
            else: even += 1
        return min(even, odd)

        # Approach 1 time O(n^2)
        # dic = collections.Counter(chips)
        # res = float('inf')
        # for i in dic:
        #     cost = 0
        #     for j in dic:
        #         if i == j: continue
        #         mod = abs(i-j) & 1
        #         cost += mod * dic[j]
        #     res = min(res, cost)
        # return res
