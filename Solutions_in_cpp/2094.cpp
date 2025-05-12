#include <bits/stdc++.h>

class Solution {
public:
    bool good(int x, int* freq) {
        std::unordered_map<int, int> temp;

        while (x != 0) {
            int d = x % 10;
            x = x / 10;
            temp[d] += 1;
        }

        for (const auto& [n, fq] : temp) {
            if (fq > freq[n]) {
                return false;
            }
        }

        return true;
    }

    std::vector<int> findEvenNumbers(std::vector<int>& digits) {
        std::array<int, 10> freq = {};

        for (int num : digits) {
            freq[num]++;
        }

        std::vector<int> res;

        for (int i = 100; i < 1000; i += 2) {
            if (good(i, freq.data())) {
                res.push_back(i);
            }
        }

        return res;
    }
};
