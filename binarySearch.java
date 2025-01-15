import java.util.Scanner;

public class binarySearch {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        sc.close();
        System.out.println(search(array, x));
    }
    public static int search(int arr[], int x){
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            int mid = end - (start + end)/2;
            if(arr[mid]==x){
                return mid;
            } else if(arr[mid]>x){
                start = mid+1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }
}
