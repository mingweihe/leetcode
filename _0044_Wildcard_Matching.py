class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        important problem
        frequently asked quiz in facebook interviews
        s = cbda
        p = *a
        i      0 0 1 2 3 4
        j      0 1 1 1 1 2
        match  0 0 1 2 3
        star  -1 0 0 0
        """
        i, j, match, star = 0, 0, 0, -1
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i, j = i+1, j+1
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else: return False
        return all(map(lambda x: x=='*', p[j:]))
