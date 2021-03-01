from collections import Counter


class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 == sum2: return 0
        if sum1 > sum2:
            sum1, sum2 = sum2, sum1
            nums1, nums2 = nums2, nums1
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        res = 0
        diff = sum2 - sum1
        for dis in xrange(5, 0, -1):
            for i in xrange(1, 6-dis+1):
                j = i + dis
                max_have = cnt1[i] + cnt2[j]
                num_need = diff / dis
                num_used = min(max_have, num_need)
                used_from1 = min(cnt1[i], num_used)
                cnt1[i] -= used_from1
                cnt2[j] -= num_used - used_from1
                diff -= num_used * dis
                res += num_used
        return -1 if diff > 0 else res
