public class insertionSort {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        sort(array);
        ArraysIO.output.print_1d(array);
    }
    public static void sort(int arr[]){
        for (int i = 1; i < arr.length; i++) {
            int j = i-1;
            int temp = arr[i];
            while (j>=0 && arr[j]>temp) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
    }
}
