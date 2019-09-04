class MyHashMap(object):
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 7000  # 1<<4
        self.bucket = [None] * self.capacity

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        h = key.__hash__() % self.capacity
        node = self.bucket[h]
        if node is None:
            self.bucket[h] = self.Entry(key, value)
            return
        while node:
            if node.key == key:
                node.value = value
                break
            if node.next is None:
                node.next = self.Entry(key, value)
            node = node.next

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        h = key.__hash__() % self.capacity
        node = self.bucket[h]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        h = key.__hash__() % self.capacity
        node = self.bucket[h]
        if node:
            if node.key == key:
                self.bucket[h] = node.next
                return
            while node.next:
                if node.next.key == key:
                    node.next = node.next.next
                    return
                node = node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
