from collections import deque
from itertools import accumulate


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ## Approach 2, convex hull window O(n)
        accums = [0] + list(accumulate(nums))
        res, dq = float('-inf'), deque()
        slope = lambda x, y: (accums[y+1] - accums[x]) / float(y-x+1)
        for i in range(k-1, len(nums)):
            while len(dq) >= 2 and slope(dq[-2], dq[-1]-1) >= slope(dq[-2], i-k):
                dq.pop()
            dq.append(i-k+1)
            while len(dq) >= 2 and slope(dq[0], dq[1]-1) <= slope(dq[0], i):
                dq.popleft()
            res = max(res, slope(dq[0], i))
        return res
    
        ## Approach 1, binary search
#         def valid(x):
#             pre, accum = 0, 0
#             pre_min = 0
#             for i in xrange(k):
#                 accum += nums[i] - x
#             if accum >= 0: return True
#             for i in xrange(k, len(nums)):
#                 accum += nums[i] - x
#                 pre += nums[i-k] - x
#                 pre_min = min(pre_min, pre)
#                 if accum - pre_min >= 0:
#                     return True
#             return False
        
#         precision = 10**-6
#         l, r = float(-10**4), float(10**4)
#         while l <= r:
#             m = l + (r-l) / 2
#             if valid(m):
#                 l = m + precision
#             else:
#                 r = m - precision
#         return r
