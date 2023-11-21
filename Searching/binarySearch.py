#Solution formatted for leetcode submission

#Binary search is O(log n) time complexity
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            #if language has a limit of size 2^32 for integers, do mid = low + ((high-low) // 2) instead
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1