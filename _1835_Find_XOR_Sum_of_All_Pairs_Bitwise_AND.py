import operator


class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # distributive property
        return reduce(operator.xor, arr1) & reduce(operator.xor, arr2)
