#bucket sort 

'''
Notes:
Only works when there is a precondition that the range of values in the array is bounded
Ex. Range of values is 0 to 100
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]

        for n in nums:
            counts[n] += 1
        
        k = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[k] = i
                k += 1
        