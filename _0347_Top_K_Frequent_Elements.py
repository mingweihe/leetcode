import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Approach 2 bucket sort
        cnt = collections.Counter(nums)
        buckets = [[] for _ in xrange(max(cnt.values()))]
        for val, f in cnt.items():
            buckets[f - 1].append(val)
        res = []
        for i in xrange(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                k -= 1
                if k == 0: return res
        return res

        # Approach 1 heap
        # cnt = collections.Counter(nums)
        # hq = []
        # for x, f in cnt.items():
        #     heapq.heappush(hq, [-f, x])
        # res = []
        # for _ in xrange(k):
        #     res.append(heapq.heappop(hq)[1])
        # return res
