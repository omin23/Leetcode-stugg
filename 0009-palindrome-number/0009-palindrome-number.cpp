class Solution {
public:
    bool isPalindrome(int x) {
        string check = to_string(x);
        for(int i = 0; i< (check.length()-1);i++){
            if(check.at(i)  != check.at(check.length()-1-i)){
                return false;
            }
        }
    return true;       
    }
};