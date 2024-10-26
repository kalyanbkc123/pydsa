class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        elements = []
        k, n = 0, 0
        m, p = len(matrix) - 1, len(matrix[0]) - 1
        index = 0

        while k <= m and n <= p:
            # Traverse from left to right
            for j in range(n, p + 1):
                elements.append(matrix[k][j])
            k += 1

            # Traverse downwards
            for i in range(k, m + 1):
                elements.append(matrix[i][p])
            p -= 1

            if k <= m:
                # Traverse from right to left
                for j in range(p, n - 1, -1):
                    elements.append(matrix[m][j])
                m -= 1

            if n <= p:
                # Traverse upwards
                for i in range(m, k - 1, -1):
                    elements.append(matrix[i][n])
                n += 1

        return elements
    
    
