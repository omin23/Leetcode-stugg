class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int sums = 0;
        for(int i = 0; i < nums.size(); i++){
            for(int j = i+1; j < nums.size(); j++){
                if (nums[j] + nums[i] == target){
                    return {i,j};
                }
            }
        }
    return {};
    }
};