class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        res = [0] * n
        
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) >= abs(nums[right]):
                val = nums[left]
                left += 1
            else:
                val = nums[right]
                right -= 1
                
            square = val**2
            res[i] = square
            
        return res
