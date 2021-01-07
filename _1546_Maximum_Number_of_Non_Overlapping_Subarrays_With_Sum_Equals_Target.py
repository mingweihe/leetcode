from itertools import accumulate
from heapq import heappush, heappop


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        hq = []
        accums = [0] + list(accumulate(nums))
        accums_idx = {}
        for i in range(len(accums)):
            cur_accum = accums[i]
            if cur_accum - target in accums_idx:
                idx = accums_idx[cur_accum - target]
                if not hq or -hq[0] <= idx:
                    heappush(hq, -i)
            accums_idx[cur_accum] = i
        return len(hq)
