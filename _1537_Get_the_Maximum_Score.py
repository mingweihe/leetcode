class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        a, b = 0, 0
        i, j = 0, 0
        MOD = 10**9 + 7
        while i < m or j < n:
            if i < m and (j == n or nums1[i] < nums2[j]):
                a += nums1[i]
                i += 1
            elif j < n and (i == m or nums1[i] > nums2[j]):
                b += nums2[j]
                j += 1
            else:
                a = b = max(a, b) + nums1[i]
                i += 1
                j += 1
        return max(a, b) % MOD
