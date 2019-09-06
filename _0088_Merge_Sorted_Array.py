class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Approach 2
        i, j = n, 0
        nums1[n:m + n] = nums1[0:m]
        while i < m + n and j < n:
            if nums1[i] < nums2[j]:
                nums1[i + j - n] = nums1[i]
                i += 1
            else:
                nums1[i + j - n] = nums2[j]
                j += 1
        if j < n: nums1[m + j:m + n] = nums2[j:n]

        # Approach 1
        # i, j = m - 1, n - 1
        # while i > -1 and j > -1:
        #     if nums1[i] > nums2[j]:
        #         nums1[i+j+1] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[i+j+1] = nums2[j]
        #         j -= 1
        # if n > -1: nums1[0:j+1] = nums2[0:j+1]
