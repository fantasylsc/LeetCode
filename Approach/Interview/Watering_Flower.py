'''

You and your friend are watering the plants. You start from the left side and your friend start from the right side. Water each plant
if you have sufficient water for it. Water each plant in one go, i.e.  you may sometimes have to refill your watering can before or after
watering a plant, even though it's not completely empty.

You start with watering the first plant and your friend start with watering the last plant. You and your friend are watering the plants simultaneously. 
How many times will you and your friend need to refill your watering cans in order to water all the plants in the row?

Example:

plants = [2, 4, 5, 1, 2], capacity1 = 5, capacity2 = 7
Return: 3

First you refill and water plants[0] and simultaneously your friend refills and waters plants[4]. Then you refill and water plants[1] and simultaneously your friend
waters plants[3]. Finally you water plants[2] together (as together you have exactly 5 units of water).

Assume that:
    N is an integer within the range [1.. 1,000];
    each element of array plants is an integer within the range[1... 1,000,000];
    capacity1 and capacity2 are intergers within the range [1... 1,000,000,000];
    both of the watering cans are large enough to fully water any single plant.

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

'''


import unittest
from collections import defaultdict

# approach 1

class Solution:
    def waterFlower(self, plants, c1, c2):
        '''
        : type plants: List[int]
        : type c1: int
        : type c2: int
        : rtype : int

        '''
        left = 0
        right = len(plants) - 1
        remain1 = c1
        remain2 = c2
        refills = 2

        while left < right:
            if plants[left] > remain1:
                remain1 = c1
                refills += 1
            if plants[right] > remain2:
                remain2 = c2
                refills += 1
            remain1 -= plants[left]
            remain2 -= plants[right]
            left += 1
            right -= 1

        if left == right:
            if plants[left] > (remain1 + remain2):
                refills += 1
                return refills
            else:
                return refills


class Test(unittest.TestCase):
    def test1(self):
        plants = [2, 4, 5, 1, 2]
        c1 = 5
        c2 = 7
        expected = 3
        sol = Solution()
        actual = sol.waterFlower(plants, c1, c2)
        self.assertEqual(actual, expected)
    def test2(self):
        plants = [2, 4, 5, 1, 2, 4]
        c1 = 5
        c2 = 7
        expected = 4 
        sol = Solution()
        actual = sol.waterFlower(plants, c1, c2)
    def test3(self):
        plants = [2, 4, 7, 1, 2]
        c1 = 6
        c2 = 7
        expected = 3
        sol = Solution()
        actual = sol.waterFlower(plants, c1, c2)

unittest.main(verbosity = 2)

