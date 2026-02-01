class Solution {
    public int diagonalSum(int[][] mat) {
        int sum = 0;
        int n = mat.length;

        for(int i = 0; i < n; i++) {
            sum += mat[i][i];              // primary diagonal
            
            if(i != n - 1 - i) {           // avoid center double count
                sum += mat[i][n - 1 - i];  // secondary diagonal
            }
        }

        return sum;
    }
}