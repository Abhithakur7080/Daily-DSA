import java.util.HashSet;

public class intersectionOfTwoArray {
    public static void main(String[] args) {
        int array1[] = ArraysIO.input.takeInput_1d();
        int array2[] = ArraysIO.input.takeInput_1d();
        intersection2(array1, array2);
    }
    public static void intersection(int arr1[], int arr2[]){
        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr2.length; j++) {
                if(arr1[i]==arr2[j]){
                    System.out.print(arr1[i] + ", ");
                    arr2[j] = Integer.MAX_VALUE;
                    return;
                }
            }
        }
    }
    public static void intersection2(int arr1[], int arr2[]){
        HashSet<Integer> set = new HashSet<>();

        for(int num : arr1){
            set.add(num);
        }

        for(int num : arr2){
            if(set.contains(num)){
                System.out.print(num + ", ");
            }
        }
    }
}
