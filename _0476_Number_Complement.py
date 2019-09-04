class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Approach 1
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return num ^ mask
        # Approach 2
        # return int(''.join(['0' if i=='1' else '1' for i in bin(num)[2:]]),2)
        # return ((1<<int(num).bit_length())-1)^num
        # Approach 3
        # mask = 1
        # while mask <= num: mask <<= 1
        # return (mask - 1) ^ num
