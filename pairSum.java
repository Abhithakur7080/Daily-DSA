import java.util.HashSet;
import java.util.Scanner;

public class pairSum {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        sc.close();
        System.out.println(pairsS(array, x));

    }
    public static int pairsS(int arr[], int x){
        int pairs = 0;
        for (int i = 0; i < arr.length-1; i++) {
            for (int j = i+1; j < arr.length; j++) {
                if(arr[i] + arr[j] == x){
                    pairs++;
                }
            }
        }
        return pairs;
    }
    public static int pairsS2(int arr[], int x) {
        int pairs = 0;
        HashSet<Integer> set = new HashSet<>();
        for (int num : arr) {
            int complement = x - num;
            if(set.contains(complement)){
                pairs++;
            }
            set.add(num);
        }
        return pairs;
    }
}
