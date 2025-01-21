public class printSpiral {
    public static void main(String[] args) {
        int matrix[][] = ArraysIO.input.takeInput_2d();
        ArraysIO.output.print_1d(print(matrix));
    }

    public static int[] print(int matrix[][]) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int result[] = new int[rows * cols];
        int k = 0;// index of result
        //direction pointers
        int top = 0;
        int bottom = rows - 1;
        int left = 0;
        int right = cols - 1;
        while (top <= bottom && left <= right) {
            // for left to right traverse(top side)
            for (int i = left; i <= right; i++) {
                result[k] = matrix[top][i];
                k++;
            }
            top++;
            // for top to bottom traverse(right side)
            for (int i = top; i <= bottom; i++) {
                result[k] = matrix[i][right];
                k++;
            }
            right--;
            if (top <= bottom) {
                // for right to left traverse(bottom side)
                for (int i = right; i >= left; i--) {
                    result[k] = matrix[bottom][i];
                    k++;
                }
                bottom--;
            }
            if(left <= right){
                // for bottom to top traverse(left side)
                for (int i = bottom; i >= top; i--) {
                    result[k] = matrix[left][i];
                    k++;
                }
                left++;
            }
        }
        return result;
    }
}
