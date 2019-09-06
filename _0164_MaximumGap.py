import math


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
            conclusion: linear sort:
                1. bucket sort
                2. radix sort
                3. counting sort
        """
        # Approach 2 bucket sort
        if len(nums) < 2: return 0
        maxi, mini = max(nums), min(nums)
        if maxi == mini: return 0
        avg_gap = int(math.ceil((maxi - mini) / float(len(nums) - 1)))
        buckets = [[None, None] for _ in xrange(len(nums))]
        for x in nums:
            bucket = buckets[(x - mini) / avg_gap]
            bucket[0] = x if bucket[0] is None else min(bucket[0], x)
            bucket[1] = x if bucket[1] is None else max(bucket[1], x)
        buckets = [x for x in buckets if x[0] is not None]
        return max(buckets[i][0] - buckets[i - 1][1] for i in xrange(1, len(buckets)))
        # Approach 1 radix sort
        # if len(nums) < 2: return 0
        # def radix_sort(A):
        #     for i in xrange(10):
        #         s = [[] for _ in xrange(10)]
        #         for x in A:
        #             s[x/10**i%10].append(x)
        #         A = [b for a in s for b in a]
        #     return A
        # sorted_array = radix_sort(nums)
        # return max(map(lambda x: x[1]-x[0], zip(sorted_array, sorted_array[1:])))
