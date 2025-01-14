import java.util.HashSet;

public class findDuplicate {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        System.out.println(duplicate2(array));

    }
    public static int duplicate(int arr[]){
        for (int i = 0; i < arr.length-1; i++) {
            for (int j = i+1; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    return arr[i];
                }
            }
        }
        return -1;
    }
    public static int duplicate2(int arr[]){
        HashSet<Integer> set = new HashSet<>();
        for (int num : arr) {
            if(set.contains(num)){
                return num;
            }
            set.add(num);
        }
        return -1;
    }
}
