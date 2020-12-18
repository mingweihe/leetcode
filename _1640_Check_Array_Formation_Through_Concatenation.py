class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        d = {x[0]:x for x in pieces}
        i, N = 0, len(arr)
        while i < N:
            if arr[i] not in d: return False
            A = d[arr[i]]
            if arr[i: i+len(A)] != A: return False
            i += len(A)
        return True
