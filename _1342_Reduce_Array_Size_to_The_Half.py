import collections


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maximum_len = len(arr) / 2
        cnts = sorted(collections.Counter(arr).values(), reverse=True)
        remained = len(arr)
        for i, x in enumerate(cnts, 1):
            remained -= x
            if remained <= maximum_len:
                return i
        return -1
