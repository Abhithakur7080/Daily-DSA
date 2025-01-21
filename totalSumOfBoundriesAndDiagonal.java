public class totalSumOfBoundriesAndDiagonal {
    public static void main(String[] args) {
        int matrix[][] = ArraysIO.input.takeInput_2d();
        System.out.println(totalSum(matrix));
    }

    public static int firstDiagonalSum(int matrix[][], int dimension) {
        /**
         * [ 2 , . , .]
         * [ . , 2 , .]
         * [ . , . , 2]
         */
        int row = 0;
        int col = 0;
        int sum = 0;
        while (row < dimension && col < dimension) {
            sum += matrix[row][col];
            row++;
            col++;
        }
        return sum;
    }

    public static int secondDiagonalSum(int matrix[][], int dimension) {
        /**
         * [ . , . , 2]
         * [ . , 2 , .]
         * [ 2 , . , .]
         */
        int row = 0;
        int col = dimension - 1;
        int sum = 0;
        while (row < dimension && col < dimension) {
            sum += matrix[row][col];
            row++;
            col--;
        }
        return sum;
    }

    public static int boundarySum(int matrix[][], int dimension) {
        /**
         * [ 2 , 2 , 2]
         * [ 2 , . , 2]
         * [ 2 , 2 , 2]
         */
        int sum = 0;
        for (int i = 1; i < dimension - 1; i++) {
            sum += matrix[0][i];// top boundary
            sum += matrix[i][0];// left boundary
            sum += matrix[dimension - 1][i];// bottom boundary
            sum += matrix[i][dimension - 1];// right boundary
        }
        return sum;
    }

    public static int totalSum(int matrix[][]) {
        int n = matrix.length;
        int sum = firstDiagonalSum(matrix, n) + secondDiagonalSum(matrix, n)
                + boundarySum(matrix, n);
                        /**
         * [ 2 ,  2  , 2]
         * [ 2 , (4) , 2] 
         * [ 2 ,  2  , 2]
         */
        // remove middle repeated when odd matrix(when 2 diagonal intersect)
        if (n % 2 != 0) {
            sum -= matrix[n / 2][n / 2];
        }
        return sum;
    }
}