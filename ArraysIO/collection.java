package ArraysIO;

public class collection {
    public static void swap(int i, int j, int arr[]){
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }
}
