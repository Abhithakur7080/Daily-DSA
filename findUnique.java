import java.util.HashMap;

public class findUnique {
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        System.out.println(unique2(array));

    }
    public static int unique(int arr[]){
        
        for(int i=0; i<arr.length; i++){
            int j;
            for(j=0; j<arr.length; j++){
                if(i!=j && arr[i]==arr[j]){
                    break;
                }
            }
            if(j==arr.length){
                return arr[i];
            }
        }
        return Integer.MAX_VALUE;
    }
    public static int unique2(int arr[]){
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int num : arr) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (int num : map.keySet()) {
            if(map.get(num) == 1){
                return num;
            }
        }
        return Integer.MAX_VALUE;
    }
}
