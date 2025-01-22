import java.util.Scanner;

public class rotateArray {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        Scanner sc = new Scanner(System.in);
        int d = sc.nextInt();
        sc.close();
        rotate2(array, d);
        ArraysIO.output.print(array);
    }

    public static void rotate(int arr[], int d) {
        // temproray hold the array
        int temp[] = new int[d];
        for (int i = 0; i < d; i++) {
            temp[i] = arr[i];
        }
        int j = 0;
        for (int i = d; i < arr.length; i++) {
            arr[j] = arr[i];
            j++;
        }
        j = 0;
        for (int i = arr.length - d; i < arr.length; i++) {
            arr[i] = temp[j];
            j++;
        }

    }

    public static void rotate2(int arr[], int d) {
        d = d % (arr.length);
        ArraysIO.collection.reverse(0, arr.length - 1, arr);
        ArraysIO.collection.reverse(0, d-1, arr);
        ArraysIO.collection.reverse(d, arr.length - 1, arr);
    }

}
