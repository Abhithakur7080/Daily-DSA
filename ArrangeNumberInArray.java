public class ArrangeNumberInArray {
    public static void main(String[] args) {
        int arr[] = ArraysIO.input.takeInput_1d();
        arrange(arr);
        ArraysIO.output.print_1d(arr);

    }
    public static void arrange(int arr[]){
        int count = 1;
        int start = 0;
        int end= arr.length - 1;
        while (start <= end) {
            if(count%2==0){
                arr[end] = count;
                end--;
            } else {
                arr[start] = count;
                start++;
            }
            count++;
        }
    }
}
