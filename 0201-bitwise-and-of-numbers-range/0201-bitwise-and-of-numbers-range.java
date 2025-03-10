class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        
        // Keep shifting left and right rightwards until they become equal
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        
        // Shift back to reconstruct the result
        return left << shift;
    }
}
