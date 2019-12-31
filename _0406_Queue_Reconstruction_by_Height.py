class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda (a, b): (-a, b))
        res = []
        for x in people:
            res.insert(x[1], x)
        return res
