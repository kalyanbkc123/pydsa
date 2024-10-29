"""

15. Array puzzle of solving celebrity problem
⮞Video Description: You are in a party of N people, where only one person is known to
everyone. Such a person may be present at the party, if yes, (s)he doesn’t know anyone at the
party. Your task is to find the celebrity at the party in Time Complexity O(n) Asked in :
Google, Flipkart, Amazon, Microsoft

"""


def celebrity(matrix, n):

    X = 0
    Y = n -1
    
    while(X < Y):
        if matrix[X][Y] == 1:
            X += 1
        else: 
            Y -= 1
            
    return X

arr = [[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]]

id  = celebrity(arr,4)

print(id)


    
    