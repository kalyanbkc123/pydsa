"""
08. Digit rearrangement method to find next greater number with same set of digits
⮞Video Description: Write an algorithm to find out next greater number to given number with
the same set of digits Asked in : Morgan Stanley, Makemytrip, Amazon


"""

def digit_rearrangment(arr):

    n = len(arr)

    # Step 1 : Find the increasing element from the left of the array
    for i in range(n-1, 0, -1):
        if arr[i] > arr[i-1]:
            break
    
    else:
            return "No increasing element Found"
        
    # Step  2 : Find the minimum element after the current element is 
    # larger than current element
    element = arr[i-1]
    min_index = i

    for j in range(i+1,n):
        if arr[j] > element and arr[j] < arr[min_index]:
            min_index = j
    

    # step-3 : Swap the elements
    arr[i-1],arr[min_index] = arr[min_index],arr[i-1]

    # step-4 : sort the subarray from index i to the end
    arr[i:n] = sorted(arr[i:n])

    return arr

# Example Usage
arr = [5,9,3,8,7,6]
result = digit_rearrangment(arr)
print("Processed array : ", result)

