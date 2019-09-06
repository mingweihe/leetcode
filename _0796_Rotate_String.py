class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # Approach 2
        return len(A) == len(B) and A in B + B

        # Approach 1
        # return True if A==B else any([A[i:]+A[:i] == B for i in range(1, len(A))])
