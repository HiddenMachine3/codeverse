class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, h = 0, cols*rows - 1
        w = cols
        print(f"w:{w} h:{h}")
        while l <= h:
            m = (l+h)//2
            print(f"m:{m} m//w:{m}//{w}={m//w} m%w:{m%w}")
            ele = matrix[m//w][m%w]

            if ele < target:
                l = m + 1
            elif ele > target:
                h = m - 1
            else:
                return True

        return False