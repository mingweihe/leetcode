class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ## Approach 2
        l, r = 0, len(arr)-1
        while l < r:
            m = l + (r-l) / 2
            if arr[m] < arr[m+1]:
                l = m + 1
            else:
                r = m
        return l
    
        ## Approach 1
        # for i in xrange(1, len(arr)-1):
        #     if arr[i-1] < arr[i] > arr[i+1]:
        #         return i
        # return -1
