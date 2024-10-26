"""
07. Linear time approach to solve jump game problem
⮞Video Description: You have an array of non-negative integers,you are initially positioned at
the first index of the array.Each element in the array represents your maximum jump length at
that position.Determine if you are able to reach the last index in O(n) Time complexity and
O(1) Space Complexity Asked in : Adobe, Intuit

"""



def linearJump(arr):

    a = arr[0]
    b = arr[0]
    n = len(arr)
    jump = 1

    for i in range(1,len(arr)):
        if(i == n - 1):
            return jump
        
        a = a - 1
        b = b - 1

        if(arr[i] > b):
            b = arr[i]
        
        if(a == 0):
            jump = jump + 1
            a = b 
    
    return jump

arr = [1,3,5,8,2,6,7,6,8,9]

jumps = linearJump(arr)

print("No of Jumps are ", jumps)