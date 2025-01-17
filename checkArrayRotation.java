public class checkArrayRotation {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        System.out.println(check(array));
    }
    public static int check(int arr[]){
        for (int i = 0; i < arr.length-1; i++) {
            if(arr[i] > arr[i+1]){
                return i+1;
            }
        }
        return 0;
    }
}
