"""
Segregation Logic To Sort The Array of 0's, 1's and 2's

We can Solve using the counting sort approach..

we have to count the number of occurencess of 0's, 1's and 2's 

then we just have to add the them to the array

Optimized Approach..
-------------------

1. if arr[mid] == 2, swap(arr,mid,high) && high--
2. if arr[mid] == 0, swap(arr, low, mid) && low++, mid++
3. if arr[mid] ==1, mid++
.

"""

def sort(arr):

    low, mid, high = 0, 0, len(arr)-1

    while(mid <= high):
        if(arr[mid] == 0):
            swap(arr, low, mid)
            low = low + 1
            mid = mid + 1
        
        elif(arr[mid] == 2):
            swap(arr,mid,high)
            high = high -1 
        
        else:
            mid = mid + 1

def swap(arr, low, high):
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp

arr = [0,0,0,2,2,2,2,1]
sort(arr)
print(arr)

