class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> hmp = new HashMap<>();

        for(int i : nums){

            hmp.put(i, hmp.getOrDefault(i, 0) + 1);
            
            if(hmp.get(i) > 1){
                return true;
            }
        }

        return false;
    }
}