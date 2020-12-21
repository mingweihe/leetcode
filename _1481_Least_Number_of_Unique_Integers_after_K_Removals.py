from collections import Counter


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        cnts = Counter(arr).items()
        cnts.sort(key=lambda x: x[1])
        for i, (_, v) in enumerate(cnts):
            if k - v == 0:
                return len(cnts) - i - 1
            elif k - v < 0:
                return len(cnts) - i
            k -= v
        return 0
