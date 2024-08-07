class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
       // zero counter
        int zc = 0;
        int index = 0;
        for(int i = 0; i < nums.size();i++){
            if(nums[i] == 0){
                if(zc == 0){
                    index = i;
                }
                zc++;
            }
        }
        cout << zc << endl;
        cout << index << endl;
        vector<int>res(nums.size(),0);
        // conditions 
        if(zc > 1){// more than one zero 
            cout << "all zeros" << endl;
            return res;
        }
        else if(zc == 1){ // only 1 zero;
            cout << "1 zeros" << endl;
            int locres = 1;
            for(int i : nums){
                if(i != 0){
                    locres *= i;
                    cout << locres << endl;
                }
            }
            res[index] = locres;
            return res;
        }

        //no zeros
        cout << "no zeros" << endl;
        //prefix calc
        res[0] = 1;
        for(int i = 1;i < nums.size();++i){
            res[i] = nums[i-1] * res[i-1];
        }
        //post fix calc
        int post = 1;
        for(int i = nums.size()-1;i > -1 ;--i){
            res[i] *= post;
            post *= nums[i];
        }


    return res;
    }
};