"""

"""


def Search_For_Element_In_Sorted_Row_And_Column(matrix : list[list[int]], N : int, value: int ):
    
    i = 0
    j = N-1
    
    while(i < N and j >= 0):
        if(matrix[i][j] == value):
            print(i ," ", j)
            return
        
        if(matrix[i][j] > value):
            j -= 1
        else:
            i += 1
    print("Value not found")
    return 

array = [[10,20,30,40],[15,25,36,46],[28,29,37,48],[32,33,39,50]]
result = Search_For_Element_In_Sorted_Row_And_Column(array,4,32)
print(result)




    