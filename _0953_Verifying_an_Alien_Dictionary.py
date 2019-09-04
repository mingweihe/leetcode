class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # Approach 2
        return words == sorted(words, key=lambda w: map(order.index, w))
        # Approach 1
        # dic = {x:i for i,x in enumerate(order)}
        # words = [[dic[w] for w in word] for word in words]
        # return all(w1<=w2 for w1, w2 in zip(words, words[1:]))
