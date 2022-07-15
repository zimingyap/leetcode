class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        min = float('inf')
        max = float('-inf')
        for i in prices:
            if i < min:
                min = i
            
            if i - min > max:
                max = i - min
                
        return max