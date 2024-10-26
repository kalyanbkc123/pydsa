"""

13. Linear time approach to solve Stock Buy Sell Problem
⮞Video Description: An array is given as Input where ith element is the price of a given stock
on day You were permitted to complete unlimited transaction. Derive an algorithm to find the
maximum profit in O(n) Time complexity and O(n) Space Complexity Asked in : Amazon, Microsoft,
Flipkart, DE-Shaw

"""

def BuyAndSellStock(prices: list[int]) -> int:
    
    # define the mini and maxi values
    mini = prices[0]
    maxi = 0
    
    for i in range(1,len(prices)):
        maxi = max(maxi,prices[i] - mini)

        mini = min(mini,prices[i])
    
    return maxi

prices = [7,1,5,3,6,4]

maxProfit = BuyAndSellStock(prices)

print(maxProfit)


        