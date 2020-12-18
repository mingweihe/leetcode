from heapq import heappush, heappop

class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hq = []
        for x in nums:
            heappush(hq, -x*2 if x & 1 else -x)
        mini = -max(hq)
        res = float('inf')
        while len(hq) == len(nums):
            cur_max = -heappop(hq)
            res = min(res, cur_max - mini)
            if cur_max & 1 == 0:
                heappush(hq, -cur_max / 2)
                mini = min(mini, cur_max / 2)
        return res
