def selectionSort(nums):
    for i in range(len(nums)):
        min_idx = i
        
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                (nums[j], nums[i]) = (nums[i], nums[j])

    return nums

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
print(selectionSort(arr))