from typing import List

class Solution:
    def diagonalPrint(self, matrix: List[List[int]]):
        # First half of diagonals (starting from rows)
        for k in range(0, len(matrix)):
            i = k
            j = 0
            while i >= 0 and j < len(matrix[0]):
                print(matrix[i][j], end=" ")
                i -= 1
                j += 1
            print()  # Newline after each diagonal

        # Second half of diagonals (starting from columns)
        for k in range(1, len(matrix[0])):
            i = len(matrix) - 1
            j = k
            while j < len(matrix[0]) and i >= 0:
                print(matrix[i][j], end=" ")
                i -= 1
                j += 1
            print()  # Newline after each diagonal

# Testing the function
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
solution.diagonalPrint(arr)
