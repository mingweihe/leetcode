class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # Approach 2
        return sorted(A, key=lambda x: x%2)
