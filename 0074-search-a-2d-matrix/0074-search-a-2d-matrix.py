class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ylen = len(matrix)
        xlen = len(matrix[0])
        total = ylen * xlen
        l,r = 0,total-1
        while l <= r:
            mid = (l+r)//2
            row = mid//xlen
            col = (mid%xlen)
            num = matrix[row][col]
            if num > target:
                r = mid-1
            elif num < target:
                l = mid+1
            elif num == target:
                return True
        return False



