package ArraysIO;

public class output {
    public static void print(int array[]) {
        System.out.print("[");
        for (int i : array) {
            System.out.print(i + (i != array[array.length - 1] ? ", " : ""));
        }
        System.out.println("]");
    }

    public static void print(int matrix[][]) {
        for (int i = 0; i < matrix.length; i++) {
            System.out.print("[");
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print(i + (i != matrix[i][matrix[0].length - 1] ? ", " : ""));
            }
            System.out.println("]");
        }
    }

    public static void print(int matrix[][][]) {
        for (int i = 0; i < matrix.length; i++) {
            System.out.print("[");
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print("[");
                for (int k = 0; k < matrix[0][0].length; k++) {
                    System.out.print(
                            matrix[i][j][k] + (matrix[i][j][k] != matrix[i][j][matrix[0][0].length - 1] ? ", " : ""));
                }
                System.out.print("]" + (j != matrix[i].length - 1 ? ", " : ""));
            }
            System.out.println("]");
        }
    }
}
