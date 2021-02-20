class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        ## Approach 2
        chars = {'&quot;': '"', '&apos;': '\'', 
                 '&gt;': '>', '&lt;': '<', '&frasl;': '/'}
        for k, v in chars.items():
            text = text.replace(k, v)
        return text.replace('&amp;', '&')

        ## Approach 1
        # chars = {'&quot;': '"', '&apos;': '\'', '&amp;': '&', 
        #          '&gt;': '>', '&lt;': '<', '&frasl;': '/'}
        # res = []
        # i, n = 0, len(text)
        # while i < n:
        #     replaced = False
        #     for k in xrange(4, 8):
        #         if text[i:i+k] in chars:
        #             res += chars[text[i:i+k]],
        #             i += k
        #             replaced = True
        #             break
        #     if not replaced:
        #         res += text[i],
        #         i += 1
        # return ''.join(res)
