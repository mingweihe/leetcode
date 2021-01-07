from collections import deque


class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ## Approach 2, monoqueue
        dq = deque()
        res = float('-inf')
        for i, x in enumerate(nums):
            while dq and i-dq[0][1] > k:
                dq.popleft()
            cur = max(x, x+(dq[0][0] if dq else 0))
            while dq and dq[-1][0] < cur:
                dq.pop()
            dq.append([cur, i])
            res = max(res, cur)
        return res
        
        
        ## Approach 1, heapq
        # hq = []
        # res = float('-inf')
        # for i, x in enumerate(nums):
        #     while hq and i-hq[0][1] > k:
        #         heappop(hq)
        #     cur = max(x, x+(-hq[0][0] if hq else 0))
        #     heappush(hq, [-cur, i])
        #     res = max(res, cur)
        # return res
