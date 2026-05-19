class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> hmp1 = new HashMap<>();
        Map<Character, Integer> hmp2 = new HashMap<>();

        if(s.length() != t.length()){
            return false;
        }

        for(int i=0; i<s.length(); i++){
            hmp1.put(s.charAt(i), hmp1.getOrDefault(s.charAt(i),0) + 1);
        }

        for(int i=0; i<t.length(); i++){
            hmp2.put(t.charAt(i), hmp2.getOrDefault(t.charAt(i),0) + 1);
        }

        return hmp1.equals(hmp2);
    }
}
