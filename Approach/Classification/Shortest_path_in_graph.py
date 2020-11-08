'''
find shortest path from start_node to end_node in a graph,
and return the path in list

'''

import unittest
from collections import deque

def construct_path(reversed_path, end_node):
    path = []
    
    current = end_node
    
    while current:
        path.append(current)
        current = reversed_path[current]
    
    path.reverse()
    
    return path
    
    
    

def get_path(graph, start_node, end_node):

    # Find the shortest route in the network between the two users
    if start_node not in graph:
        raise
    if end_node not in graph:
        raise
    
    q = deque()
    q.append(start_node)
    reversed_path = {start_node: None}
    
    while q:
        current = q.popleft()
        
        if current == end_node:
            return construct_path(reversed_path, end_node)
        
        for node in graph[current]:
            if node not in reversed_path:
                q.append(node)
                reversed_path[node] = current
                

    return None









# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)




