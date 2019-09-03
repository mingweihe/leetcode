class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(format(n, '032b')[::-1], 2)
