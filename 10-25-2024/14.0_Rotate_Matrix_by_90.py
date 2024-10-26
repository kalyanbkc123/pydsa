

def RotateMatrixBy90(matrix : list[list[int]], N: int):
    
    for i in range(0,N // 2):
        for j in range(i,N-i-1):
            
            temp = matrix[j][N-i-1]
            
            matrix[j][N-1-i] = matrix[i][j]
            
            matrix[i][j] = matrix[N-1-j][i]
            
            matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
            
            matrix[N-1-i][N-1-j] = temp


matrix = [[1,2,3],[4,5,6],[7,8,9]]

RotateMatrixBy90(matrix,3)

print(matrix)
             
              
            
            
            
            
            
    
    
    
    