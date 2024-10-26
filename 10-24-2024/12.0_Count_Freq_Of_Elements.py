def elementFreq(arr):
    
    n = len(arr)
       
    for i in range(0,n):
        arr[i] -= 1
    
    for i in range(0,n):
        arr[arr[i] % n] = n + arr[arr[i] % n]
        
    for i in range(0,n):
        print((i+1) , " " , arr[i] // n)


arr = [2,3,3,2,5]
count  = elementFreq(arr)


    

        
    