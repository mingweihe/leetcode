class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        following the natural order of reading a passage...
        """
        # Approach 2
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == len(bits) - 1
        # Approach 1
        # cnt = 0
        # for x in bits[::-1][1:]:
        #     if x == 0:
        #         break
        #     cnt += 1
        # return cnt % 2 == 0
