import collections


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = collections.Counter(arr).values()
        return len(cnt) == len(set(cnt))
