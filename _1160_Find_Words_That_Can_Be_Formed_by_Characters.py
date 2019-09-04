import collections


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        dic = collections.Counter(chars)
        for x in words:
            cur = dic.copy()
            ok = True
            for c in x:
                if c not in cur or cur[c] == 0:
                    ok = False
                    break
                cur[c] -= 1
            if ok: res += len(x)
        return res
