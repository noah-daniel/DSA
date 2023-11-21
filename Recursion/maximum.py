#find the maximum number in a list using recursion
def maximum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        if nums[0] > maximum(nums[1:]):
            return nums[0]
        else:
            return maximum(nums[1:])

print(max([1,6,2,20,10]))