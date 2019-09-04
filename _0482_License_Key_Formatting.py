class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # Approach 1
        s = S.replace('-', '')[::-1].upper()
        return '-'.join(s[i:i + K] for i in range(0, len(s), K))[::-1]
        # Approach 2
        # S = S.replace('-', '').upper()[::-1]
        #
        # def chunks():
        #     for i in range(0, len(S), K): yield S[i:i + K]
        # return '-'.join(chunks())[::-1]
