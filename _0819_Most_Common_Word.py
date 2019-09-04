import re
import collections


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Approach 2
        ban = set(banned)
        p = re.findall('\w+', paragraph.lower())
        counters = collections.Counter(x for x in p if x not in ban)
        return counters.most_common()[0][0]
        # Approach 1
        # res_word = ''
        # res_frequent = 0
        # dic_res = {}
        # dic_banned = {x:True for x in banned}
        # for word in re.split('!|\?|\'|,|;|\.', paragraph):
        #     words = word.lower().strip().split()
        #     for w in words:
        #         if not dic_banned.get(w):
        #             dic_res[w] = dic_res.get(w, 0) + 1
        #             if dic_res[w] > res_frequent:
        #                 res_word = w
        #                 res_frequent = dic_res[w]
        # return res_word
