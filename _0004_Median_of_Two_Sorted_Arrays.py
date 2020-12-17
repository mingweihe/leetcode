class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        time complexity: O(log(min(m, n))
        """
        ## Approach 2, simplified
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        k = (m+n+1) / 2
        l, r = 0, m
        while l < r:
            m1 = l + (r-l) / 2
            n1 = k - m1
            if nums1[m1] > nums2[n1-1]:
                r = m1
            else: l = m1 + 1

        c1 = max(nums1[l-1] if l > 0 else float('-inf'), nums2[k-l-1] if k-l-1 >= 0 else float('-inf'))
        if (m+n) & 1: return c1
        c2 = min(nums1[l] if l < m else float('inf'), nums2[k-l] if k-l < n else float('inf'))
        return (c1+c2) / 2.0
        
        ## Approach 1
        # x, y = len(nums1), len(nums2)
        # if x > y:
        #     nums1, nums2 = nums2, nums1
        #     x, y = y, x
        # low, high = 0, x
        # while low <= high:
        #     partitionX = (low+high)/2
        #     partitionY = (x+y+1)/2-partitionX
        #     maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX-1]
        #     minRightX = float('inf') if partitionX == x else nums1[partitionX]
        #     maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY-1]
        #     minRightY = float('inf') if partitionY == y else nums2[partitionY]
        #     if maxLeftX <= minRightY and maxLeftY <= minRightX:
        #         if (x+y) % 2 == 0:
        #             return (max(maxLeftX,maxLeftY)+min(minRightX, minRightY))/float(2)
        #         else:
        #             return float(max(maxLeftX, maxLeftY))
        #     elif maxLeftX > minRightY:
        #         high = partitionX - 1
        #     else:
        #         low = partitionX + 1
