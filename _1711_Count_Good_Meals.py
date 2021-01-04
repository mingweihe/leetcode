from collections import defaultdict


class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        dic = defaultdict(int)
        meal_sums = [1<<i for i in xrange(22)]
        res = 0
        for x in deliciousness:
            for possible in meal_sums:
                res += dic[possible-x]
            dic[x] += 1
        return res % MOD
