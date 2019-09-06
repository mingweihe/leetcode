class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Approach 2
        words.sort(key=lambda w: (-len(w), w))
        wordset = set(words)
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word
        return ""

        # Approach 1
        # res = ''
        # valid = set([''])
        # words.sort(key=lambda w: (len, w))
        # for x in words:
        #     if x[:-1] in valid:
        #         valid.add(x)
        #         if len(x) > len(res):
        #             res = x
        # return res
