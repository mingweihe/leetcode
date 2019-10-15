import collections


class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        maintaining maximum frequency and freq dictionary
        time O(n)
        """
        res = 0
        dict = collections.defaultdict
        cnt, freq = dict(int), dict(int)
        max_f = 0
        for i, x in enumerate(nums):
            cnt[x] += 1
            freq[cnt[x] - 1] -= 1
            freq[cnt[x]] += 1
            max_f = max(max_f, cnt[x])
            if freq[max_f] * max_f == i or (freq[max_f - 1] + 1) * (max_f - 1) == i \
                    or max_f == 1: res = i + 1
        return res
