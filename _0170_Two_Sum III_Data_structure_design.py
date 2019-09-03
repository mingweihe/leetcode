class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        self.max = float('-inf')
        self.min = float('inf')

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.data[number] = self.data.get(number, 0) + 1
        if number > self.max:
            self.max = number
        if number < self.min:
            self.min = number

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value > self.max * 2 or value < self.min * 2:
            return False
        dic = self.data
        for k in dic:
            target = value - k
            if target in dic and (target != k or dic[k] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
