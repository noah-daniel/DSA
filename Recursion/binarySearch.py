#binary search with recursion
def binarySearch(nums, l, r, target):
    if l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binarySearch(nums, l, mid - 1, target)
        else:
            return binarySearch(nums, mid + 1, r, target)
        
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10
print(binarySearch(arr, 0, len(arr)-1, x))