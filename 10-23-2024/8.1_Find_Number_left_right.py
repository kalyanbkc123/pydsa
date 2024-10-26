
"""
⮞Assignment Problem: We have an array, we have to find an element before which all elements
are less than it, and after which all are greater than it. Finally, return the index of the
element, if there is no such element, then return -1: Time complexity O(n) and Space
Complexity O(n)

"""

def findNumber(arr):

    n = len(arr)

    # Initialize left array
    left = [0]*n
    left[0] = float('-inf')

    for i in range(1,n):
        left[i] = max(left[i-1],arr[i-1])

    right = float('inf') 

    for i in range(n-1,-1,-1):
        if(left[i] < arr[i] < right):
            return i
        right = min(right,arr[i])
    
    return -1


arr = [6,2,5,4,7,9,11,8,10]

print("the number is ",arr[findNumber(arr)])



