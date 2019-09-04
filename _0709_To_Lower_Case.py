class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # Approach 3
        return str.lower()
        # Approach 2
        # return ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in str])
        # Approach 1
        # res = ''
        # for c in str:
        #     ascii_num = ord(c)
        #     if 64 < ascii_num < 90:
        #         c = chr(ascii_num + 32)
        #     res += c
        # return res

