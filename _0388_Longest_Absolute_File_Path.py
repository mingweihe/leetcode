class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        input = input.split('\n')
        res, lvl_len_dic = 0, {-1: -1}
        for s in input:
            len_name = len(s) - s.rfind('\t') - 1
            lvl = s.count('\t')
            cur_len = lvl_len_dic[lvl - 1] + len_name + 1
            if '.' not in s:
                lvl_len_dic[lvl] = cur_len
            else:
                res = max(res, cur_len)
        return res
