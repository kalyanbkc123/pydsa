"""

⮞Assignment Problem: Given an array consists of non-negative integers, your task is to count
the number of triplets chosen from the array that can make triangles if we take them as side
lengths of a triangle Time Complexity O(n2) Space Complexity O(1)

"""

def TrianglesCount(arr):
    n = len(arr)

    arr.sort()

    count = 0 

    for i in range(0,n-2):
        for j in range(i+1,n):
            k = j + 1
            while(k < n and arr[i] + arr[j] > arr[k]):
                k = k + 1
            
            count = count + (k-1)-j
    
    return count


arr = [12,35,255,250,95,90,38]

print("Count No. Of Triangels ", TrianglesCount(arr))