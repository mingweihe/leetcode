class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        L = len(text)
        accum = [1] * L
        block_num_dic = {}
        for i in xrange(L - 2, -1, -1):
            if text[i] == text[i + 1]:
                accum[i] = accum[i + 1] + 1
        for i in xrange(1, L):
            if text[i] == text[i - 1]:
                accum[i] = accum[i - 1]
            else:
                block_num_dic[text[i - 1]] = block_num_dic.get(text[i - 1], 0) + 1
        block_num_dic[text[-1]] = block_num_dic.get(text[-1], 0) + 1
        res = max(accum)
        for i in xrange(1, L - 1):
            if text[i] != text[i - 1] and text[i - 1] == text[i + 1]:
                carry = 1 if block_num_dic[text[i - 1]] > 2 else 0
                res = max(res, accum[i - 1] + accum[i + 1] + carry)
            else:
                carry = 1 if block_num_dic[text[i - 1]] > 1 else 0
                res = max(res, accum[i - 1] + carry)
        carry = 1 if block_num_dic[text[-1]] > 1 else 0
        res = max(res, accum[-1] + carry)
        return res
