public class pushZeroToEnd {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        zeroToEnd(array);
        ArraysIO.output.print(array);
    }
    public static void zeroToEnd(int arr[]){
        int nonZeroCount = 0;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] != 0){
                ArraysIO.collection.swap(i, nonZeroCount, arr);
                nonZeroCount++;
            }
        }
    }
}
