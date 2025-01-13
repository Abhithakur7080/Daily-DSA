package assets;

public class utils {
    public static void swap(int a, int b){
        //METHOD - 1
        // int temp = a;
        // a = b;
        // b = temp;

         //METHOD - 2
        a = a + b;
        b = a - b;
        a = a - b;
    }
}
