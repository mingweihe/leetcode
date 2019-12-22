import collections


class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        dic = collections.defaultdict(int)
        for i in xrange(len(s) - minSize + 1):
            for j in xrange(minSize, maxSize + 1):
                if i + j > len(s): break
                cur = s[i:i + j]
                if len(set(cur)) > maxLetters: break
                dic[cur] += 1
        return max(dic.values() or [0])
