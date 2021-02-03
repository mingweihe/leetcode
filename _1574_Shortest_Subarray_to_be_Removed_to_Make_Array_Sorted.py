class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Approach 2, O(n)
        n = len(arr)
        left, right = 0, n-1
        while left < n-1 and arr[left] <= arr[left+1]: left += 1
        while right > 0 and arr[right] >= arr[right-1]: right -= 1
        res = n - max(left+1, n-right)
        if res == 0: return 0
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j-i-1)
                i += 1
            else: j += 1
        return res
    
        # Approach 1, O(n*log(n))
#         n = len(arr)
#         increasing_at_left = 1
#         for i in xrange(1, n):
#             if arr[i] >= arr[i-1]: increasing_at_left += 1
#             else: break
                
#         increasing_at_right = 1
#         for i in xrange(n-2, -1, -1):
#             if arr[i] <= arr[i+1]: increasing_at_right += 1
#             else: break
                
#         left, right = increasing_at_left - 1, n-increasing_at_right
#         increasing_at_sides = 0
#         if left < right:
#             A, B = arr[:left+1], arr[right:]
#             for i, x in enumerate(A):
#                 pos_in_B = bisect_left(B, x)
#                 increasing_at_sides = max(increasing_at_sides, i+1 + len(B)-pos_in_B)
                
#         return n - max(increasing_at_left, increasing_at_right, increasing_at_sides)
