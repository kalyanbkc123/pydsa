"""
⮞Assignment Problem: There are N children standing in a line with some rating value. You want
to distribute a minimum number of candies to these children such that:
Each child must have at least one candy.
The children with higher ratings will have more candies than their neighbors.
You need to write a program to calculate the minimum candies you must give.

"""

def sumCandy(ratings, n):
    
    sum  = 0
    left = [1] * n
    right = [1] * n

    # left traversal
    for i in range(1,n):
        if(ratings[i] > ratings[i-1]):
            left[i] = left[i-1] + 1
    
    # right traversal
    for i in range(n-2,-1,-1):
        if(ratings[i] > ratings[i+1]):
            right[i] = right[i+1] + 1
    
    # find max sum
    for i in range(0,n):
        sum += max(left[i],right[i])
    
    return sum


arr = [1,5,0,2]

sum = sumCandy(arr,len(arr))

print(sum)