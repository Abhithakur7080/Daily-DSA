public class sort01 {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        sort2(array);
        ArraysIO.output.print_1d(array);
    }
    public static void sort(int arr[]){
        int countZeros = 0;
        for (int num : arr) {
            if (num==0){
                countZeros++;
            }
        }
        for (int i = 0; i < arr.length; i++) {
            if(countZeros>0){
                arr[i] = 0;
                countZeros--;
            } else {
                arr[i] = 1;
            }
        }
    }
    //for 0,1,2 all three
    public static void sort2(int arr[]){
        int temp[] = new int[3];
        for (int num : arr) {
            temp[num]++;
        }
        for (int i = 0; i < arr.length; i++) {
            if(temp[0]>0){
                arr[i] = 0;
                temp[0]--;
            } else if(temp[1]>0){
                arr[i] = 1;
                temp[1]--;
            } else {
                arr[i] = 2;
                temp[2]--;
            }
        }
    }
}
