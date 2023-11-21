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