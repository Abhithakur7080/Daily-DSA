public class selectionSort {
        public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        sort(array);
        ArraysIO.output.print(array);
    }
    public static void sort(int arr[]){
        for (int i = 0; i < arr.length; i++) {
            int minValue = Integer.MAX_VALUE;
            int minIndex = -1;
            //find minimum value
            for (int j = i; j < arr.length; j++) {
                if(arr[j]<minValue){
                    minValue = arr[j];
                    minIndex = j;
                }
            }
            //swap with minimun value
            ArraysIO.collection.swap(minIndex, i, arr);
        }
    }
}
