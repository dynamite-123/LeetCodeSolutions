    class Solution {
        public int[] twoSum(int[] nums, int target) {
            // int[] res = new int[2];
            // number, ind hashmap
            HashMap<Integer, Integer> hm = new HashMap<>();
            for(int i = 0; i < nums.length; i++){
                if(hm.containsKey(target - nums[i])){
                    // res = new int[] {hm.get(target - nums[i]), i};
                    return new int[] {hm.get(target - nums[i]), i};
                }
                hm.put(nums[i], i);
            }
            // return res;
            return new int[] {};
        }
    }