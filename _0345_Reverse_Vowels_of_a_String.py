class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l, r = 0, len(s) - 1
        v = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        while l < r:
            if not s[l].lower() in v:
                l += 1
            elif not s[r].lower() in v:
                r -= 1
            else:
                s[l], s[r], l, r = s[r], s[l], l + 1, r - 1
        return ''.join(s)
