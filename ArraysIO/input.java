package ArraysIO;
import java.util.Scanner;
public class input{
    static Scanner sc = new Scanner(System.in);
    public static int[] takeInput_1d() {
        System.out.println("Enter the size of 1D array");
        int size = sc.nextInt();
        int array[] = new int[size];
        for(int i=0; i< size; i++){
            System.out.print("Enter index-" + i + ": ");
            array[i] = sc.nextInt();
        }
        return array;
    }
    public static int[][] takeInput_2d() {
        System.out.println("Enter the no of rows");
        int row = sc.nextInt();
        System.out.println("Enter the no of colums");
        int col = sc.nextInt();

        int matrix[][] = new int[row][col];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print("Enter index- (" + i + "," + j + ") :");
                matrix[i][j] = sc.nextInt();
            }
        }
        return matrix;
    }
    public static int[][][] takeInput_3d() {
        System.out.println("Enter the no of items in x-dimensions");
        int x = sc.nextInt();
        System.out.println("Enter the no of items in y-dimensions");
        int y = sc.nextInt();
        System.out.println("Enter the no of items in z-dimensions");
        int z = sc.nextInt();

        int matrix[][][] = new int[x][y][z];

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                for (int k = 0; k < z; k++) {
                    System.out.print("Enter index- (" + i + "," + j + "," + k + ") :");
                    matrix[i][j][k] = sc.nextInt();
                }
            }
        }
        return matrix;
    }
}