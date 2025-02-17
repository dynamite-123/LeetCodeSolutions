class Solution {
public:
    int reverse(int x) {
        long int r = 0;

        while(x != 0){
            r = r * 10 + x % 10;
            x = x/10;
        }

        return (r < INT_MIN || r > INT_MAX) ? 0 : r; // - from <climits> header file


    }
};