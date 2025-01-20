public class largestRowOrColumn {
    public static void main(String[] args) {
        int matrix[][] = ArraysIO.input.takeInput_2d();
        String result = largestSum(matrix);
        System.out.println(result);
    }

    public static String largestSum(int matrix[][]) {
        int largest_row = Integer.MIN_VALUE;
        int largest_col = Integer.MIN_VALUE;
        int largest_row_index = 0;
        int largest_col_index = 0;

        if (matrix.length < 1) {
            return "row 0 0";
        }

        // Calculate row sum
        for (int i = 0; i < matrix.length; i++) {
            int rowSum = 0;
            for (int j = 0; j < matrix[0].length; j++) {
                rowSum += matrix[i][j];
            }
            if (rowSum > largest_row) {
                largest_row = rowSum;
                largest_row_index = i;
            }
        }

        // Calculate column sum
        for (int i = 0; i < matrix[0].length; i++) {
            int colSum = 0;
            for (int j = 0; j < matrix.length; j++) {
                colSum += matrix[j][i];
            }
            if (colSum > largest_col) {
                largest_col = colSum;
                largest_col_index = i;
            }
        }

        if (largest_row >= largest_col) {
            return "row " + largest_row_index + " " + largest_row;
        } else {
            return "column " + largest_col_index + " " + largest_col;
        }
    }
}
