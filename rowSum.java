public class rowSum{
    public static void rowWiseSum(int[][] mat) {
		if(mat.length ==0) {
			return;
		}
		int sum = 0;
		for(int i=0;i<mat.length;i++) {
			for(int j = 0;j<mat[0].length;j++) {
				sum += mat[i][j];
			}
			System.out.print(sum + " ");
			sum = 0;
		}
		System.out.println();
	}
}