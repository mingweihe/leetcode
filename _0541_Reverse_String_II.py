class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Approach 1
        res = ''
        for i in range(0,len(s), k): res+=s[i:i+k][::-1] if not i%(2*k) else s[i:i+k]
        return res

        # Approach 2
        # return ''.join(s[i:i + k][::-1] if not i % (2 * k) else s[i:i + k] for i in range(0, len(s), k))
