class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        # Approach 2, bit manipulation
        needs = 0
        for num in data:
            if needs > 0:
                if num & 192 != 128: return False
            elif needs == 0:
                if num & 128 == 0:
                    pass
                elif num & 224 == 192:
                    needs = 1
                elif num & 240 == 224:
                    needs = 2
                elif num & 248 == 240:
                    needs = 3
                else:
                    return False
            else:
                return False
            if num & 192 == 128: needs -= 1
        return needs == 0

        # Approach 1, bin + zfill + startswith
        # needs = 0
        # for num in data:
        #     byte = bin(num)[2:][-8:].zfill(8)
        #     if needs > 0:
        #         if byte[:2] != '10': return False
        #     elif needs == 0:
        #         if byte.startswith('0'): pass
        #         elif byte.startswith('110'): needs = 1
        #         elif byte.startswith('1110'): needs = 2
        #         elif byte.startswith('11110'): needs = 3
        #         else: return False
        #     else: return False
        #     if byte[:2] == '10': needs -= 1
        # return needs == 0
