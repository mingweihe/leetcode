class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
            1. find i largest numbers' array from nums1, k-i nums' array from nums2
            2. merge tow parts' arrays to a largest combined number array
            3. compare different number array, return the maximum
        """
        m, n = len(nums1), len(nums2)
        res = [0] * k
        for i in xrange(max(0, k - n), min(m + 1, k + 1)):
            temp = self.merge(self.max_array(nums1, i), self.max_array(nums2, k - i))
            if self.greater(temp, 0, res, 0): res = temp
        return res

    def greater(self, nums1, i, nums2, j):
        m, n = len(nums1), len(nums2)
        while i < m and j < n and nums1[i] == nums2[j]:
            i += 1
            j += 1
        if j == n or i < m and nums1[i] > nums2[j]:
            return True
        return False

    def merge(self, nums1, nums2):
        L = len(nums1) + len(nums2)
        res = [0] * L
        i, j = 0, 0
        for k in xrange(L):
            if self.greater(nums1, i, nums2, j):
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1
        return res

    def max_array(self, nums, k):
        res = [0] * k
        L = len(nums)
        j = 0
        for i in xrange(L):
            while j > 0 and L - i > k - j and nums[i] > res[j - 1]:
                j -= 1
            if j < k:
                res[j] = nums[i]
                j += 1
        return res
