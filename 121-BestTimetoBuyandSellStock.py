from typing import List

class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')  # Initialize with infinity to ensure any price will be lower
        max_profit = 0  # Initialize max profit to 0
        
        for price in prices:
            # Update the minimum price seen so far
            if price < min_price:
                min_price = price
            
            # Calculate the profit if we sell at the current price
            potential_profit = price - min_price
            
            # Update the maximum profit seen so far
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit

sol = Solution()
print(sol.maxProfit([3,10,4,5]))