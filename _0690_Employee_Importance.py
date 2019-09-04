# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        ed = {e.id: e for e in employees}
        stack = [ed[id]]
        res = 0
        while stack:
            emp = stack.pop()
            res += emp.importance
            for i in emp.subordinates:
                stack.append(ed[i])
        return res
