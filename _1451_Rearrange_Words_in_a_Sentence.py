from collections import defaultdict


class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        dic = defaultdict(list)
        word_list = text.split()
        word_list[0] = word_list[0].lower()
        for word in word_list:
            dic[len(word)] += word,
        res = []
        for wl in sorted(dic.keys()):
            res += dic[wl]
        res[0] = res[0].capitalize()
        return ' '.join(res)
