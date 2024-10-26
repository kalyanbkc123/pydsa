
"""

<<<<<<< HEAD
05. Maximum Value in an array of Increasing and Decreasing using Binary Search
⮞Video Description: One array of integers is given as an input ,which is initially increasing
and then decreasing or it can be only increasing or decreasing , you need to find the maximum
value in the array in O(Log n) Time complexity and O(1) Space Complexity Asked in : Amazon,
Microsoft, Uber

=======
>>>>>>> 72165569936df7d4c9f20e35b5a3cc6a00fdd935
In the Question We are given an array, Which is increasing and decreasing or vice versa 
We have to return a Maximum Value in the Array

Approach: 
    Our Approach is First Finding the pattern where the Maximum Value Could Lie..
    we have a pattern 
    we use start end pointers, calculate mid,,
    if left value of mid is less and more is more then we are in the increasing side of the array, better to move towards
    right so move => start = mid +1.
    if left value of mid is more and right value is less, then we are in the decreasing side of the array, 
    better to move towards left => end = mid - 1
    if the left element is less and right element is more, we return the array.


    left is less and right is more => right
    left is more and right is less => left
    left is less and right is less => return the max of two elements..

"""


def FindMaxiumValue(arr, start, end):
    if start == end:
        return arr[start]
    if end == start + 1:
        if arr[start] >= arr[end]:
            return arr[start]
        else: 
            return arr[end]
    
    mid = start + end // 2

    if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1] :
        return arr[mid]
    if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
        return FindMaxiumValue(arr,mid+1,end)
    else:
        return FindMaxiumValue(arr,start,mid-1)

arr = [6,9,15,25,35,50,41,29,23,6]

print(FindMaxiumValue(arr,0,10))
