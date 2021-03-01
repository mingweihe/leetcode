class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        res = 0
        rules = {'type': 0, 'color': 1, 'name': 2}
        for item in items:
            res += item[rules[ruleKey]] == ruleValue
        return res
