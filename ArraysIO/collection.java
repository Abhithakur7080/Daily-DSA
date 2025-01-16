package ArraysIO;

public class collection {
    // public static void main(String[] args) {
    //     int array[] = ArraysIO.input.takeInput_1d();
    //     reverse(0, array.length/2, array);
    //     ArraysIO.output.print_1d(array);
    // }
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
