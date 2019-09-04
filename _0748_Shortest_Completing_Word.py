import collections


class Solution(object):
    def shortestCompletingWord(self, lp, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # Approach 2
        cnt_d = collections.Counter([x for x in lp.lower() if x.isalpha()])
        words.sort(key=len)
        for w in words:
            if all(w.count(x) >= cnt_d[x] for x in cnt_d):
                return w

        # Approach 1
        # cnt_d = collections.Counter([x for x in lp.lower() if x.isalpha()])
        # return min([w for w in words if not cnt_d-collections.Counter(w)], key=len)
