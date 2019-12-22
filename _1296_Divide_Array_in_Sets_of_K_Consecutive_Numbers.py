import collections


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0: return False
        cnts = collections.Counter(nums)
        keys = sorted(cnts.keys())
        for start in keys:
            if cnts[start] == 0: continue
            while cnts[start] != 0:
                for i in xrange(k):
                    cur = start + i
                    if cnts[cur] == 0: return False
                    cnts[cur] -= 1
        return True
