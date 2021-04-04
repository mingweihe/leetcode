from bisect import bisect_left


class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sorted_nums1 = sorted(nums1)
        def get_closest(x):
            idx = bisect_left(sorted_nums1, x)
            if idx == len(sorted_nums1):
                return sorted_nums1[-1]
            if idx == 0:
                return sorted_nums1[0]
            if abs(sorted_nums1[idx]-x) < abs(sorted_nums1[idx-1]-x):
                return sorted_nums1[idx]
            return sorted_nums1[idx-1]
        
        total_diff = sum(abs(nums1[i]-nums2[i]) for i in xrange(len(nums1)))
        can_reduce_most = 0
        for i in xrange(len(nums1)):
            closest = get_closest(nums2[i])
            cur = abs(nums1[i]-nums2[i]) - abs(closest-nums2[i])
            can_reduce_most = max(can_reduce_most, cur)
        return (total_diff - can_reduce_most) % (10**9+7)
