
public class ArraySum {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        System.out.println(sum(array));
    }
    public static int sum(int arr[]){
        int sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return sum;
    }
}
