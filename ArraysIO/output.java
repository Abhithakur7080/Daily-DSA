package ArraysIO;
public class output {
    public static void print_1D(int array[]) {
        System.out.print("[");
        for (int i : array) {
            System.out.print(i + (i != array[array.length - 1] ? ", " : " "));
        }
        System.out.println("]");
    }
}
