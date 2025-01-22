package StringIO;
import java.util.Scanner;
public class input{
    static Scanner sc = new Scanner(System.in);
    public static String[] takeInput_1d() {
        System.out.println("Enter the size of 1D array");
        int size = sc.nextInt();
        String array[] = new String[size];
        for(int i=0; i< size; i++){
            System.out.print("Enter index-" + i + ": ");
            array[i] = sc.next();
        }
        return array;
    }
    public static String[][] takeInput_2d() {
        System.out.println("Enter the no of rows");
        int row = sc.nextInt();
        System.out.println("Enter the no of colums");
        int col = sc.nextInt();

        String matrix[][] = new String[row][col];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print("Enter index- (" + i + "," + j + ") :");
                matrix[i][j] = sc.next();
            }
        }
        return matrix;
    }
}