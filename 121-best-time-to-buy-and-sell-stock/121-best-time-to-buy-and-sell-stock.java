class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1){
            return 0;
        }
        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int i =0; i<prices.length; i++){
            if (prices[i] < min)
                min = prices[i];
            
            int max1 = prices[i] - min;
            
            if (max1 > max ){
                max = max1;
            }
        }
        return max;
    }
}