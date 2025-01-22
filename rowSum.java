public class rowSum {
	public static void main(String[] args) {
		int matrix[][] = ArraysIO.input.takeInput_2d();
		int result[] = rowWiseSum(matrix);
		ArraysIO.output.print(result);
	}

	public static int[] rowWiseSum(int[][] mat) {
		if (mat.length == 0) {
			return new int[0];
		}
		int result[] = new int[mat.length];
		for (int i = 0; i < mat.length; i++) {
			int sum = 0;
			for (int j = 0; j < mat[0].length; j++) {
				sum += mat[i][j];
			}
			result[i] = sum;
		}
		return result;
	}
}