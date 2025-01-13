public class swapAlternate {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        swapAlter(array);
        ArraysIO.output.print_1D(array);
    }
    public static void swapAlter(int arr[]){
        for (int i = 0; i < arr.length-1; i+=2) {
            ArraysIO.collection.swap(i, i+1, arr);
        }
    }
}
