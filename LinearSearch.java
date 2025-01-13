import java.util.Scanner;

import ArraysIO.input;

public class LinearSearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int array[] = input.takeInput_1d();
        int x = sc.nextInt();
        sc.close();
        System.out.println(search(array, x));
    }
    public static int search(int arr[], int x){
        for (int i=0; i<arr.length; i++) {
            if(arr[i]== x) return i;
        }
        return -1;
    }
}
