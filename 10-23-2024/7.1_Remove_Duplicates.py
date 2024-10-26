
"""
⮞Assignment Problem: Given a sorted array, remove the duplicates in place such that each
element appear only once and return the new length. Do not allocate extra space for another
array, Time complexity O(n) and Space complexity O(1)

"""

def removeDuplicates(arr):
    n = len(arr)
    if(n == 0 or n == 1):
        return len(arr)
    
    j = 0

    for i in range(0,(len(arr)-1)):
        if(arr[i] != arr[i+1]):
            arr[j] = arr[i]
            j = j+1
    
    arr[j] = arr[n-1]
    j=j+1

    return j

arr = [1,2,2,3,4,5,5,5]
lenth = removeDuplicates(arr)
print(arr,lenth)

