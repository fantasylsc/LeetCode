'''

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

'''

# solution 1: loop through cornor index, move down left

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        result, intermediate = [], []
        
        for d in range(m + n - 1):
            intermediate.clear()
            
            r, c = 0 if d < n else d - n + 1, d if d < n else n - 1
            
            while r < m and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
                
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
                
        return result
        
# solution 2: the same diagonal has the same sum of r and c, 
#             use a dictionary to record the items in the same diagonal

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        d={}
		#loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
				#if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
				#If you've already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(matrix[i][j])
		# we're done with the pass, let's build our answer array
        ans= []
		#look at the diagonal and each diagonal's elements
        for entry in d.items():
			#each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
			#snake time, look at the diagonal level
            if entry[0] % 2 == 0:
				#Here we append in reverse order because its an even numbered level/diagonal. 
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans





