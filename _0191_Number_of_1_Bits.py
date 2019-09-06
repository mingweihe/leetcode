class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 2
        return bin(n).count('1')

        # Approach 1
        # return sum(map(int, list(bin(n)[2:])))
