        int dfs(int i, int total, int N) {
            if (i == N) {
                return total;
            }

            return (dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total), N);
        }