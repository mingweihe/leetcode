from collections import defaultdict


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.idxs = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        res = not self.idxs[val]
        self.vals += val,
        self.idxs[val].add(len(self.vals)-1)
        return res

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.idxs[val]:
            out_idx = self.idxs[val].pop()
            in_val = self.vals[-1]
            self.vals[out_idx] = self.vals[-1]
            self.vals.pop()
            self.idxs[in_val].add(out_idx)
            self.idxs[in_val].discard(len(self.vals))
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.vals)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
