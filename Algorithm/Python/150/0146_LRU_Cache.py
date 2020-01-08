
'''

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''

'''
Python OrderedDict()

dic = OrderedIdct()
dic[key] = value
dic.pop(key)
dic.popitem(last = False) # Default pop last item

'''
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            val = self.dic.pop(key)
            self.dic[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None: # consider capacity
        if key in self.dic:
            self.dic.pop(key)
            self.dic[key] = value
        else:
            if len(self.dic) == self.capacity:
                self.dic.popitem(last = False) # dic.popitem()
                self.dic[key] = value
            else:
                self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        
        
