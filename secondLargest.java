public class secondLargest {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        System.out.println(sLargest(array));
    }
    public static int sLargest(int arr[]){
        if(arr.length < 2){
            return -1;
        }
        int l = arr[0];
        int sl = Integer.MIN_VALUE;

        for (int i = 1; i < arr.length; i++) {
            if(arr[i]>l){
                sl = l;
                l = arr[i];
            } else if(arr[i] > sl && arr[i] < l){
                sl = arr[i];
            }
        }
        return sl;
    }
}
