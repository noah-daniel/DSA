class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        hi = len(matrix) - 1

        while low <= hi:
            mid = (low + hi) // 2
            if target < matrix[mid][0]:
                hi = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                break

        if not(low <= hi):
            return False
            
        sub_low = 0
        sub_hi = len(matrix[low]) - 1

        while sub_low <= sub_hi:
            sub_mid = (sub_low + sub_hi) // 2
            if target < matrix[mid][sub_mid]:
                sub_hi = sub_mid - 1
            elif target > matrix[mid][sub_mid]:
                sub_low = sub_mid + 1
            else:
                return True

        return False