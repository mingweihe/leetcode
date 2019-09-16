import collections


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        res, pool = [], []
        mid = ''
        odd = 0
        for k, v in cnt.items():
            if v & 1:
                mid += k
                odd += 1
            if odd == 2: return res
            pool += [k] * (v / 2)
        used = [False] * len(pool)
        self.backtracking(res, '', used, pool, mid)
        return res

    def backtracking(self, res, cur, used, pool, mid):
        if len(cur) == len(pool):
            res.append(cur + mid + cur[::-1])
            return
        for i in xrange(len(pool)):
            if i > 0 and not used[i - 1] and pool[i] == pool[i - 1]: continue
            if not used[i]:
                used[i] = True
                cur += pool[i]
                self.backtracking(res, cur, used, pool, mid)
                used[i] = False
                cur = cur[:-1]
