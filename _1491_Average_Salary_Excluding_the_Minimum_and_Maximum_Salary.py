class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return (sum(salary)-max(salary)-min(salary)) / float(len(salary)-2) 
