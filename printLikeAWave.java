public class printLikeAWave {
    public static void main(String[] args) {
        int matrix[][] = ArraysIO.input.takeInput_2d();
        ArraysIO.output.print(print(matrix));
    }

    public static int[] print(int matrix[][]) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int result[] = new int[rows * cols];
        int k = 0;
        /**
         * [ #  , # -> #  , #]
         * [ #  , # ,  #  , #]
         * [ # -> # ,  # -> #]
         */

        for (int j = 0; j < cols; j++) { // Column-wise iteration
            if (j % 2 == 0) {
                // Top to bottom for even-indexed columns
                for (int i = 0; i < rows; i++) {
                    System.out.print("top to bottom - " + matrix[i][j]);
                    result[k] = matrix[i][j];
                    k++;
                }
            } else {
                // Bottom to top for odd-indexed columns
                for (int i = rows - 1; i >= 0; i--) {
                    System.out.print("bottom to top - " + matrix[i][j]);
                    result[k] = matrix[i][j];
                    k++;
                }
            }
            System.out.println();
        }

        return result;
    }
}
