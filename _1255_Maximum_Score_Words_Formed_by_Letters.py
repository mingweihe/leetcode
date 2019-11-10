import collections


class Solution(object):
    def maxScoreWords(self, words, letters, scores):
        """
        :type words: List[str]
        :type letters: List[str]
        :type scores: List[int]
        :rtype: int
            solution: backtracking,
            tracking the words, each word can be selected or not
            on the other hand, reduce the problem by using Counter
        """
        self.res = 0
        cnts = collections.Counter(letters)

        def bt(idx, _cnts, score):
            if idx == len(words):
                self.res = max(self.res, score)
                return
            bt(idx + 1, _cnts, score)
            word_cnt = collections.Counter(words[idx])
            if all(_cnts[c] >= word_cnt[c] for c in word_cnt):
                cur_score = sum(v * scores[ord(k) - 97] for k, v in word_cnt.items())
                bt(idx + 1, _cnts - word_cnt, score + cur_score)

        bt(0, cnts, 0)
        return self.res
