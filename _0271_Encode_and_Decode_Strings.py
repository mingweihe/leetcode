class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        return ''.join(map(lambda x: `len(x)` + '/' + x, strs))

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res, i = [], 0
        while i < len(s):
            ind_slash = s.index('/', i)
            size = int(s[i:ind_slash])
            res.append(s[ind_slash + 1:ind_slash + size + 1])
            i = ind_slash + size + 1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
