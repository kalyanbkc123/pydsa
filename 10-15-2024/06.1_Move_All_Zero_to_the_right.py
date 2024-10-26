"""

⮞Assignment Problem: Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements in O(n) Time complexity and O(1)
Space complexity with single traversal allowed

"""

def moveToRight(arr):
    count = 0 

    for i in range(len(arr)):
        
        if (arr[i] != 0):  
            arr[count] = arr[i]        
            count = count +1

    while count < len(arr):
        arr[count] = 0
        count += 1


arr = [1,2,3,3,0,3,0]
moveToRight(arr)
print(arr)