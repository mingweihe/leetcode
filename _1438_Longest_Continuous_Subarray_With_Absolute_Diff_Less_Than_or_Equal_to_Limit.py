from collections import deque


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        # Approach 2, double deque, O(n)
        minq, maxq = deque(), deque()
        i = 0
        for x in nums:
            while minq and x < minq[-1]: minq.pop()
            while maxq and x > maxq[-1]: maxq.pop()
            minq.append(x)
            maxq.append(x)
            if maxq[0] - minq[0] > limit:
                if nums[i] == minq[0]: minq.popleft()
                if nums[i] == maxq[0]: maxq.popleft()
                i += 1
        return len(nums) - i
            
        ## Approach 1, two heapq, O(n*logn)
        # maxh, minh = [], []
        # res = j = 0
        # for i, x in enumerate(nums):
        #     heappush(maxh, [-x, i])
        #     heappush(minh, [x, i])
        #     while -maxh[0][0] - minh[0][0] > limit:
        #         j = min(maxh[0][1], minh[0][1]) + 1
        #         while maxh[0][1] < j: heappop(maxh)
        #         while minh[0][1] < j: heappop(minh)
        #     res = max(res, i-j+1)
        # return res
