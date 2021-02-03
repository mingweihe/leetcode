from bisect import bisect_left, bisect_right


class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Approach 1, O(n*log(n))
        n = len(arr)
        increasing_at_left = 1
        for i in xrange(1, n):
            if arr[i] >= arr[i-1]: increasing_at_left += 1
            else: break
                
        increasing_at_right = 1
        for i in xrange(n-2, -1, -1):
            if arr[i] <= arr[i+1]: increasing_at_right += 1
            else: break
                
        left, right = increasing_at_left - 1, n-increasing_at_right
        increasing_at_sides = 0
        if left < right:
            A, B = arr[:left+1], arr[right:]
            for i, x in enumerate(A):
                pos_in_B = bisect_left(B, x)
                increasing_at_sides = max(increasing_at_sides, i+1 + len(B)-pos_in_B)
                
        return n - max(increasing_at_left, increasing_at_right, increasing_at_sides)
