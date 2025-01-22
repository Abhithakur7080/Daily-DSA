package ArraysIO;

public class collection {
    public static void swap(int i, int j, int arr[]){
        // arr[i] = arr[i] + arr[j];
        // arr[j] = arr[i] - arr[j];
        // arr[i] = arr[i] - arr[j];
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void reverse(int start, int end, int array[]){
        while (start <= end) {
            swap(start++, end--, array);
        }
    }
    
}
