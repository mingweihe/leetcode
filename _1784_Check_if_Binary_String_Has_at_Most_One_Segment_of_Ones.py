class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## Approach 3
        return '01' not in s
    
        ## Approach 2
        # return not s.strip('0').strip('1')
    
        ## Approach 1
        # return s.strip('0').count('0') == 0
