"""
⮞Assignment Problem: We rotate an ascending order sorted array at some point unknown to user.
So for instance, 3 4 5 6 7 might become 5 6 7 3 4. Modify binary search algorithm to find an
element in the rotated array in O(log n) time and O(1) Space complexity

"""

# Time : O(logn)
# Space : O(1)

def Search_In_Rotated(arr,start,end,value):
    
    mid = (start + end ) // 2
    
    # check for the value 
    if(arr[mid] == value):
        return mid
    
    # left half is sorted
    if(arr[start] <= arr[mid]):
        # check in sorted half
        if(arr[start] <= value < arr[mid]):
            return Search_In_Rotated(arr,start,mid-1,value)
        # search in right half
        else:
            return Search_In_Rotated(arr,mid+1,end,value)
    
    # right half is sorted
    if(arr[mid] <= arr[end]):
        # check in sorted half
        if(arr[mid] < value <= arr[end]):
            return Search_In_Rotated(arr,mid+1,end,value)
        else:
            return Search_In_Rotated(arr,start,mid-1,value)


arr = [5,6,7,8,3,4]

index = Search_In_Rotated(arr,0,len(arr)-1,7)

print(index)


        