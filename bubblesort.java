public class bubblesort {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        sort(array);
        ArraysIO.output.print(array);
    }
    public static void sort(int arr[]){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length-1; j++) {
                if(arr[j] > arr[j+1]){
                   ArraysIO.collection.swap(j, j+1, arr);
                }
            }
        }
    }
}
