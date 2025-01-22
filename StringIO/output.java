package StringIO;
public class output {
    public static void print_1d(String array[]) {
        System.out.print("[");
        for (String i : array) {
            System.out.print(i + (i != array[array.length - 1] ? ", " : ""));
        }
        System.out.println("]");
    }
    public static void print_2d(String matrix[][]) {
        for (int i=0; i < matrix.length; i++) {
            System.out.print("[");
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print(matrix[i][j] + (matrix[i][j] != matrix[i][matrix[0].length - 1] ? ", " : ""));
            }
            System.out.println("]");
        }
    }
}
