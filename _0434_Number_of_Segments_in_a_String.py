class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach 1
        return sum(s[i] != ' ' and (i == 0 or s[i - 1] == ' ') for i in range(len(s)))

        # Approach 2
        # return len(s.split())
