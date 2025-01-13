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
}