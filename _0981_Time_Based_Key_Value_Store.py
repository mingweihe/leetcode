import collections
import bisect


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
            problem solving idea: separating timestamp and values in different dics
        """
        self.timestamps = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.timestamps[key] += timestamp,
        self.values[key] += value,

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
            idea: bisect.bisect is default bisect_right
                index will greater than 0 if it exits in the list
                so if it's not 0, index - 1 would the index smaller than
                or equal with the select value
        """
        idx = bisect.bisect(self.timestamps[key], timestamp)
        return self.values[key][idx - 1] if idx else ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
