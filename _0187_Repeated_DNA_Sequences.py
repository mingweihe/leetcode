class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Approach 2
        res, seen = set(), set()
        for i in xrange(len(s)-9):
            cur = s[i:i+10]
            if cur in seen: res.add(cur)
            else: seen.add(cur)
        return list(res)
        # Approach 1
        # dic = {}
        # res = []
        # for i in xrange(len(s)-9):
        #     cur = s[i:i+10]
        #     if cur in dic:
        #         if dic[cur] == 1:
        #             res.append(cur)
        #             dic[cur] = 0
        #     else: dic[cur] = 1
        # return res
