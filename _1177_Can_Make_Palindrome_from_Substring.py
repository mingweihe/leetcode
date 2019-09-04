class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
            read description read descriptions!
            rearrange! up to!
        """
        L = len(queries)
        cur, cnt = [0]*26, [[0]*26]
        for c in s:
            cur[ord(c)-97] += 1
            cnt.append(cur[:])
        res = [False]*L
        for i, x in enumerate(queries):
            l, r, k = x[0], x[1], x[2]
            num_odd = sum((b-a)&1 for a, b in zip(cnt[l], cnt[r+1]))
            res[i] = k >= num_odd / 2
        return res
