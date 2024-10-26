"""

"""

"""
# Counting Sort

Time : O(nlogn)
Space : O(1)

1. First Sort the array
2. if adjacnent elements are same then increment the count
3. elif adjancent elements are not same, check count < n // 2 
    then make current element majority and decremnt the count
4. return majorityElement

"""

def findElement1(arr:list[int]) -> int:
    
    n = len(arr)
    
    arr.sort()
    
    count = 0
    
    for i in range(1,n):
        
        if(arr[i] == arr[i-1]):
            count += 1
            #majority = arr[i]
        
        if(arr[i] != arr[i-1] and count < n//2):
            majority = arr[i]
            count = 1
    
    return majority

"""
Use HashMap (dictionary)
1. declare the hash map
2. store the freq of element
3. find if freq ? length // 2
4. retur count

"""

def findMajorityElement(nums: list[int]) -> int:
    # Declare a dictionary
    count = {}
    n = len(nums)
    
    # Count occurrences of each element
    for i in range(n):
        if nums[i] in count:
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1
    
    # Check for majority element
    for key in count:
        if count[key] > n // 2:
            return key



## Optimized Approach :: 



def findElement(arr: list[int]) -> int:
    
    n = len(arr)
    
    # declare first element as majority element
    majElement = arr[0]
    
    count = 0
    
    for j in range(1,n):
        if(majElement == arr[j]):
            count += 1
        else: 
            count = count - 1
        if(count == 0):
            majElement = arr[j]
            count += 1
    
    return majElement

arr = [2,3,3,2,2,5,2,3,1,2,2]

val = findMajorityElement(arr)

print(val)


    