#quicksort: done in LeetCode submission form
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):
            if len(nums) < 2:
                return nums
            else:
                pivot = random.choice(nums)
                left, mid, right = [], [], []
                for num in nums:
                    if num < pivot: left.append(num)
                    if num == pivot: mid.append(num)
                    if num > pivot: right.append(num)
            return quicksort(left) + mid + quicksort(right)
        return quicksort(nums)
    

#Alternative Quicksort solution
    
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, arr, left, right):
        if left < right:
            partition_pos = self.partition(arr, left, right)
            self.quickSortHelper(arr, left, partition_pos - 1)
            self.quickSortHelper(arr, partition_pos + 1, right)

    def partition(self, arr, left, right):
        i = left
        j = right - 1
        pivot = arr[right]

        while i < j:
            while arr[i].key < pivot.key and i < right:
                i +=1
            while arr[j].key >= pivot.key and j > left:
                j -= 1

            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]

        if arr[i].key >= pivot.key:
            arr[i], arr[right] = arr[right], arr[i]
        
        return i


