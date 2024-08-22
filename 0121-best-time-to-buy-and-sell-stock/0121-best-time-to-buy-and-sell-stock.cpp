class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int max = 0;
        while(r < prices.size()){
            if(prices[l] < prices[r]){
              int diff = prices[r] -  prices[l];
              if(diff > max){max = diff;}
            }
            else{
                l = r;
            }
            r++;
        }
        return max;

    }
};

 // int size = prices.size();
        // int max = 0;
        // for(int r = 0; r < size-1;r++){
        //     for(int l = r+1; l < size; l++){
        //         int sum = prices[l] - prices[r];
        //         if(sum > max){
        //             max = sum;
        //         }
        //     }
        // }

        // return max;