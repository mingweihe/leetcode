class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Approach 2
        g.sort()
        s.sort()
        i=j=0
        lg,ls=len(g),len(s)
        while i < lg and j < ls:
            if g[i] <= s[j]: i+=1
            j+=1
        return i

        # Approach 1
        # g.sort()
        # s.sort()
        # i = j = 0
        # lg, ls = len(g), len(s)
        # while i < lg:
        #     while (j + 1) < ls and s[j] < g[i]: j += 1
        #     if j < ls and s[j] >= g[i]:
        #         i += 1
        #         j += 1
        #     else:
        #         break
        # return i
