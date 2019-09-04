import re


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return re.sub('\.', '[.]', address)
