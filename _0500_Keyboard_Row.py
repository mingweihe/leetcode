import re


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Approach 1
        # res=[]
        # alphabet=['qwertyuiop','asdfghjkl','zxcvbnm']
        # for i in words:
        #     for j in alphabet:
        #         s = set(i)
        #         L = len(s)
        #         t = 0
        #         for k in s:
        #             if k.lower() in j: t+=1
        #         if t == L:
        #             res.append(i)
        #             break
        # return res
        # Approach 2
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)