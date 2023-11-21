#binary search with recursion

def binarySearch(arr, target):
    def recursive_helper(low, high):
        if low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return recursive_helper(low, mid - 1)
            else:
                return recursive_helper(mid + 1, high)
    return recursive_helper(0, len(arr) - 1)

arr = [ 2, 3, 4, 10, 40 ]
x = 10

print(binarySearch(arr, x))