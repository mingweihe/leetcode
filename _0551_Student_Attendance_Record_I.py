class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Approach 1
        # return s.count('A') < 2 and not re.compile('L{3,}').search(s)
        # Approach 2
        return len(s.split('A')) < 3 and s.find('LLL') == -1
