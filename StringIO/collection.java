package StringIO;

public class collection {
    public static void swap(int i, int j, String arr[]){
        String temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    public static void swap(int i, int j, char arr[]){
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    public static void reverse(int start, int end, String array[]){
        while (start <= end) {
            swap(start++, end--, array);
        }
    }
    public static void reverse(int start, int end, char array[]){
        while (start <= end) {
            swap(start++, end--, array);
        }
    }
    public static void reverse(int start, int end, String str){
        while (start <= end) {
            swap(start++, end--, str.split(""));
        }
    }
    
}
