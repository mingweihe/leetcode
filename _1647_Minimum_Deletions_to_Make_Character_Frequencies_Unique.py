from collections import Counter


class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        freqs = sorted(Counter(s).items(), key=lambda x: -x[1])
        last_freq = freqs[0][1]
        for i in xrange(1, len(freqs)):
            cur_freq = freqs[i][1]
            if cur_freq >= last_freq:
                num_del = cur_freq - last_freq + 1
                res += num_del
                if cur_freq - num_del == 0: continue
                last_freq = cur_freq - num_del
            else: last_freq = cur_freq
        return res
