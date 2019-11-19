import collections


class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
            union find / disjoint set + backtracking
        """
        dic = collections.defaultdict(str)
        for x, y in synonyms: dic[x], dic[y] = x, y

        def find(key):
            if key != dic[key]:
                dic[key] = find(dic[key])
            return dic[key]
        for x, y in synonyms:
            x, y = find(x), find(y)
            if x == y: continue
            dic[x] = y
        graphs = collections.defaultdict(set)
        for k in dic: graphs[find(k)].add(k)

        def bt(cur, pos, ans):
            if pos == len(text):
                ans += ' '.join(cur),
                return
            if text[pos] not in dic:
                cur += text[pos],
                bt(cur, pos+1, ans)
                cur.pop(),
                return
            for w in graphs[dic[text[pos]]]:
                cur += w,
                bt(cur, pos+1, ans)
                cur.pop()
        res = []
        text = text.split()
        bt([], 0, res)
        return sorted(res)
