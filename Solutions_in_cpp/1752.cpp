    class Solution {
    public:
        bool check(vector<int>& nums) {
            int flag = 0;
            for(int i=1; i<nums.size(); i++){
                if(nums[i]<nums[i-1]){
                    flag++;
                    if(flag == 2){
                        return false;
                    }
                }
            }
            if(flag == 0){
                return true;
            }
            if(nums[0] < nums[nums.size()-1]){
                return false;
            }
            return true;
        }
        
    };