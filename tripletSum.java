import java.util.HashMap;
import java.util.Scanner;

public class tripletSum {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        sc.close();
        System.out.println(tripletsS3(array, x));
    }

    public static int tripletsS(int arr[], int x) {
        int tripletCount = 0;
        for (int i = 0; i < arr.length - 2; i++) {
            for (int j = i + 1; j < arr.length - 1; j++) {
                for (int k = j + 1; k < arr.length; k++) {
                    if (arr[i] + arr[j] + arr[k] == x) {
                        tripletCount++;
                    }
                }
            }
        }
        return tripletCount;
    }
    public static int tripletsS2(int arr[], int x) {
        int tripletCount = 0;
        for (int i = 0; i < arr.length - 2; i++) {
            int new_arr[] = new int[10000];
            for (int j = i + 1; j < arr.length; j++) {
                int complement = x - arr[i] - arr[j];
                if (complement >= 0) {
                    tripletCount += new_arr[complement];
                }
                new_arr[arr[j]]++;
            }
        }
        return tripletCount;
    }
    public static int tripletsS3(int arr[], int x) {
        int tripletCount = 0;
        for (int i = 0; i < arr.length - 2; i++) {
           HashMap<Integer, Integer> map = new HashMap<>();
            for (int j = i + 1; j < arr.length; j++) {
                int complement = x - arr[i] - arr[j];
                if (map.containsKey(complement)) {
                    tripletCount += map.get(complement);
                }
                map.put(arr[j], map.getOrDefault(arr[j], 0)+1);
            }
        }
        return tripletCount;
    }
    
}