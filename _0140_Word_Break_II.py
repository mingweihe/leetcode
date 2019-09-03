class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s, set(wordDict), {}, 0)

    def helper(self, s, wd, cache, start):
        if start in cache: return cache[start]
        res = []
        if start == len(s): res.append('')
        for i in xrange(start + 1, len(s) + 1):
            first_half = s[start:i]
            if first_half in wd:
                sub_set = self.helper(s, wd, cache, i)
                for second_half in sub_set:
                    if second_half: second_half = ' ' + second_half
                    res.append(first_half + second_half)
        cache[start] = res
        return res
