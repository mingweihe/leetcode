class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ## Approach 2, heapq, O(n*logn)
        hq = []
        for i, x in enumerate(nums):
            while hq and i-hq[0][1] > k:
                heappop(hq)
            cur_best = -hq[0][0] + x if hq else x
            heappush(hq, [-cur_best, i])
        return cur_best

        ## Approach 1, monoqueue, O(n)
        # maxq = deque()
        # for i, x in enumerate(nums):
        #     if maxq and i-maxq[0][0] > k:
        #         maxq.popleft()
        #     cur_best = maxq[0][1] + x if maxq else x
        #     while maxq and cur_best > maxq[-1][1]:
        #         maxq.pop()
        #     maxq.append([i, cur_best])
        # return maxq[-1][1]
