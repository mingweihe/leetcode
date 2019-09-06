import re


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        paths = re.split('/+', path)
        for x in paths:
            if x == '..':
                if stack:
                    stack.pop()
            elif x != '.' and x != '':
                stack.append(x)
        return '/' + '/'.join(stack)
