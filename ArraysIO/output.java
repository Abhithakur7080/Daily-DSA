package ArraysIO;
// quick travels -> forEach loop [1,2,3,4,5,6,7,8,9]
public class output {
    public static void print_1d(int array[]) {
        System.out.print("[");
        for (int i : array) {
            System.out.print(i + (i != array[array.length - 1] ? ", " : ""));
        }
        System.out.println("]");
    }
    public static void print_2d(int matrix[][]) {
        for (int i=0; i < matrix.length; i++) {
            System.out.print("[");
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print(i + (i != matrix[i][matrix[0].length - 1] ? ", " : ""));
            }
            System.out.println("]");
        }
    }
}
