class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        S1 = (C - A) * (D - B)
        S2 = (G - E) * (H - F)
        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bottom = max(B, F)
        overlap = 0
        if left < right and bottom < top:
            overlap = (right - left) * (top - bottom)
        return S1 + S2 - overlap
