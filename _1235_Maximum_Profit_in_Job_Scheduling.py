import bisect


class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
            key point: order by endTime, binary search by start time
            sorting + new ascending order value array + binary search
            time O(n*log(n)) space O(n)
        """
        jobs = sorted(zip(endTime, startTime, profit))
        dp = [[0, 0]]
        for e, s, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp += [e, dp[i][1] + p],
        return dp[-1][1]
