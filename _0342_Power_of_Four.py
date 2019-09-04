class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = int(num).bit_length()-1
        return num == 2**l and l % 2 == 0
