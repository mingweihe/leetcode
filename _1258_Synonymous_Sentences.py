import collections


class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        dic = collections.defaultdict(set)
        for x, y in synonyms:
            if x in dic or y in dic:
                sets = dic[x] or dic[y]
                sets.add(y)
                sets.add(x)
                dic[x] = dic[y] = sets
            else: dic[x] = dic[y] = set([x, y])

        def bt(cur, pos):
            if pos == len(text):
                self.res += ' '.join(cur),
                return
            if text[pos] not in dic:
                cur += text[pos],
                bt(cur, pos+1)
                cur.pop(),
                return
            for w in dic[text[pos]]:
                cur += w,
                bt(cur, pos+1)
                cur.pop()
        self.res = []
        text = text.split()
        bt([], 0)
        return sorted(self.res)
