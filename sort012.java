public class sort012 {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        sort(array);
        ArraysIO.output.print_1d(array);
    }
    public static void sort(int arr[]){
        int index0 = 0;
        int index2 = arr.length -1;
        int i = 1;
        while (i < arr.length) {
            if(arr[i] == 0 && i > index0){
                ArraysIO.collection.swap(index0, i, arr);
                index0++;
            } else if(arr[i] == 2 && i < index2){
                ArraysIO.collection.swap(index2, i, arr);
                index2--;
            } else {
                i++;
            }
            
        }
    }
}
