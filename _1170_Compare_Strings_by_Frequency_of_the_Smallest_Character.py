import bisect


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        optimization : for code concise consideration,
            collections.Counter is a good choice.
        """
        def f(s):
            smallest = s[0]
            dic = {}
            for x in s:
                dic[x] = dic.get(x, 0) + 1
                smallest = min(smallest, x)
            return dic[smallest]

        words = list(map(f, words))
        words.sort()
        queries = map(f, queries)
        res = [0] * len(queries)
        L = len(words)
        for i, x in enumerate(queries):
            res[i] = L - bisect.bisect_right(words, x)
        return res
