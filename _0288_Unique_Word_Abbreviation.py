def get_key(word):
    L = len(word)
    if L < 3: return word
    return word[0] + `L - 2` + word[-1]


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        d = self.d = {}
        for word in dictionary:
            key = get_key(word)
            if key in d:
                if d[key] != word:
                    d[key] = ''
            else:
                d[key] = word

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        key = get_key(word)
        return key not in self.d or self.d[key] == word

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
