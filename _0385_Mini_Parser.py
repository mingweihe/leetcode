# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger(object):
    def __init__(self, value=None):
        pass

    def isInteger(self):
        pass

    def add(self, elem):
        pass

    def setInteger(self, value):
        pass

    def getInteger(self):
        pass

    def getList(self):
        pass


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0] != '[': return NestedInteger(int(s))
        res = NestedInteger()
        stack = [res]
        start = 1
        for i in xrange(1, len(s)):
            if s[i] == '[':
                cur = NestedInteger()
                stack[-1].add(cur)
                stack.append(cur)
                start = i + 1
            elif s[i] in (',', ']'):
                if i > start:
                    stack[-1].add(NestedInteger(int(s[start:i])))
                start = i + 1
                if s[i] == ']': stack.pop()
        return res
