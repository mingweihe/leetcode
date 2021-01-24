class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        xor_all = 0
        for i in xrange(1, len(encoded)+2):
            xor_all ^= i
        xor_others = 0
        for i in xrange(1, len(encoded), 2):
            xor_others ^= encoded[i]
        first = xor_all ^ xor_others
        res = [first]
        for x in encoded:
            res += res[-1] ^ x,
        return res
