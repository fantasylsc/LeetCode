
'''

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                index1 = i - 1
                break
            else:
                if i == 1:
                    nums[::] = nums[:: - 1]
                    return
                continue
                
        for i in range(n - 1, index1, -1):
            if nums[i] > nums[index1]:
                index2 = i
                break
            else:
                continue
                
        nums[index1], nums[index2] = nums[index2], nums[index1]
        nums[index1 + 1: n] = nums[n: index1: - 1]
        



