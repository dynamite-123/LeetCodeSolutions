class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long res = 0, high = 0, diff = 0;

        for (long long it : nums) {
            res = max({res, it * diff});
            diff = max({diff, high - it});
            high = max({it, high});
        }
        return res;
    }
};