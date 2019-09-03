class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt = [0]*128
        start = j = 0
        minimum = float('inf')
        total = len(t)
        for x in t: cnt[ord(x)] += 1
        for i in xrange(len(s)):
            cur_i_key = ord(s[i])
            if cnt[cur_i_key] > 0: total -= 1
            cnt[cur_i_key] -= 1
            while total == 0:
                if i-j+1 < minimum:
                    minimum = i-j+1
                    start = j
                cur_j_key = ord(s[j])
                cnt[cur_j_key] += 1
                if cnt[cur_j_key] > 0: total += 1
                j += 1
        return '' if minimum == float('inf') else s[start:start+minimum]
