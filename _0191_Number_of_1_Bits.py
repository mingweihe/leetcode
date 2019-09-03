class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 1
        # return sum(map(int, list(bin(n)[2:])))
        # Approach 2
        return bin(n).count('1')
