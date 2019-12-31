class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # merge sort O(n*log(n))
        pre_sum = [0]
        for x in nums:
            pre_sum += pre_sum[-1] + x,

        def sort(lo, hi):
            mid = (lo + hi) / 2
            if mid == lo: return 0
            cnt = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            for left in pre_sum[lo:mid]:
                while i < hi and pre_sum[i] - left < lower: i += 1
                while j < hi and pre_sum[j] - left <= upper: j += 1
                cnt += j - i
            pre_sum[lo:hi] = sorted(pre_sum[lo:hi])
            return cnt

        return sort(0, len(pre_sum))
