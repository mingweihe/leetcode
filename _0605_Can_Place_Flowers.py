class Solution(object):
    def canPlaceFlowers(self, A, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        L = len(A) - 1
        for i, x in enumerate(A):
            if x == 0 and (i == 0 or A[i - 1] == 0) and (i == L or A[i + 1] == 0):
                A[i], n = 1, n - 1
        return n <= 0
