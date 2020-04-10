'''

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

 

Note:

    1 <= A[i], B[i] <= 6
    2 <= A.length == B.length <= 20000


'''

# greedy approach
# notice that if the job can be done, all A or B should be A[0] or B[0]

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            rotations_a = rotations_b = 0
            for i in range(n):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    rotations_a += 1
                elif B[i] != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)
        
        n = len(A)
        rotations = check(A[0])
        
        if rotations != -1:
            return rotations
        else:
            return check(B[0])



# backtracking
# TLE

# class Solution:
#     def minDominoRotations(self, A: List[int], B: List[int]) -> int:
#         self.res = float('inf')
#         rotation = self.backtrack(A[:], B[:], 0, 0)
#         if self.res != float('inf'):
#             return self.res
#         else:
#             return -1
        
#     def backtrack(self, A, B, start, rotation):
#         if len(set(A[:])) == 1 or len(set(B[:])) == 1:
#             self.res = min(self.res, rotation)
#             return
#         for i in range(start, len(A)):
#             A[i], B[i] = B[i], A[i]
#             rotation += 1
#             self.backtrack(A[:], B[:], start + 1, rotation)
#             A[i], B[i] = B[i], A[i]
#             rotation -= 1
        




