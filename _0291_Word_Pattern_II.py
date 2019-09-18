class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.is_match(pattern, 0, str, 0, dict(), set())

    def is_match(self, pat, i, string, j, dic, sets):
        if i == len(pat) and j == len(string): return True
        if i == len(pat) or j == len(string): return False
        c = pat[i]
        if c in dic:
            s = dic[c]
            if not string.startswith(s, j): return False
            return self.is_match(pat, i + 1, string, j + len(s), dic, sets)
        for k in xrange(j, len(string)):
            s = string[j:k + 1]
            if s in sets: continue
            dic[c] = s
            sets.add(s)
            if self.is_match(pat, i + 1, string, k + 1, dic, sets): return True
            dic.pop(c)
            sets.discard(s)
        return False
