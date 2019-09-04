"""
This is open addressing method.
(Another ofen used method is separate linked list)
---------
According to leetcoder Cai's coding style.
We can also define some constant variable or methods on top of class.
While we're designing a hash table class, so it's better to define
every method or constant variable inside of the class.
"""


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 8
        self.size = 0  # is only used for having a size() function
        self.occupied_size = 0
        self.table = [None] * self.capacity
        self.load_factor = .75

    def _collision_processing(self, h):
        return (h * 5 + 1) % self.capacity

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.occupied_size / float(self.capacity) >= self.load_factor:
            self.capacity <<= 1
            new_table = [None] * self.capacity
            for x in self.table:
                if x is not None and x != -1:
                    h = x.__hash__() % self.capacity
                    while new_table[h] is not None:
                        h = self._collision_processing(h)
                    new_table[h] = x
            self.table = new_table
            self.occupied_size = self.size
        h = key.__hash__() % self.capacity
        while self.table[h] is not None:
            if self.table[h] == key: return
            h = self._collision_processing(h)
        self.table[h] = key
        self.size += 1
        self.occupied_size += 1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = key.__hash__() % self.capacity
        while self.table[h] is not None:
            if self.table[h] == key:
                self.table[h] = -1  # tombstone
                self.size -= 1
                return
            h = self._collision_processing(h)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        # print(self.table)
        h = key.__hash__() % self.capacity
        while self.table[h] is not None:
            if self.table[h] == key: return True
            h = self._collision_processing(h)
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
