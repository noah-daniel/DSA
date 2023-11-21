def selectionSort(nums):
    for i in range(len(nums)):
        min_idx = i
        
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                (nums[j], nums[i]) = (nums[i], nums[j])

    return nums

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
print(selectionSort(arr))


#alternate solution

def findSmallest(nums):
    smallest = nums[0]
    smallest_idx = 0
    for i in range(len(nums)):
        if nums[i] < smallest:
            smallest_idx = i
            smallest = nums[i]
    return smallest_idx

def altSelectionSort(nums):
    sortedNums = []
    for i in range(len(nums)):
        smallest = findSmallest(nums)
        sortedNums.append(nums.pop(smallest))
    return sortedNums

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
print(altSelectionSort(arr))