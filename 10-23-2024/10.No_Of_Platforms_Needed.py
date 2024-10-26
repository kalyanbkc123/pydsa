

"""

"""

def No_Of_Platforms(arrival, departure):

    departure.sort()

    i, j = 0, 0
    platforms = 0
    maxPlatforms = 0

    n = len(arrival)

    while(i < n and j < n):
        if(arrival[i] < departure[i]):
            platforms += 1
            i += 1
            maxPlatforms = max(maxPlatforms, platforms)
        else:
            platforms -= 1
            j += 1
    return maxPlatforms

arrival = [1.0, 1.4, 1.5, 2.0, 2.15, 4.0]
departure = [1.10, 3.0, 2.20, 2.30, 3.15, 6.0]

# Call the function and print the result
print("No of Platforms needed:", No_Of_Platforms(arrival, departure))