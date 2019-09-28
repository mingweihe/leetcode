class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
            key point: backward traversal is a good approach for maintaining
                values when doing in-place operations in array
        """
        # Approach 2 backward traversal
        L, num_zeros = len(arr), arr.count(0)
        for i in xrange(L-1, -1, -1):
            if i + num_zeros < L:
                arr[i+num_zeros] = arr[i]
            if arr[i] == 0:
                num_zeros -= 1
                if i + num_zeros < L:
                    arr[i+num_zeros] = 0

        # Approach 1 forward traversal
        L = len(arr)
        left, right = 0, L-1
        num_dup = 0
        while left < right:
            if arr[left] == 0:
                right -= 1
                num_dup += 1
            left += 1
        arr[num_dup:] = arr[:L-num_dup]
        i, j = 0, num_dup
        while j < L:
            if arr[j] != 0:
                arr[i] = arr[j]
                i += 1
            else:
                arr[i] = 0
                if i+1 < L: arr[i+1] = 0
                i += 2
            j += 1
