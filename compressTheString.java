import java.util.Scanner;

public class compressTheString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(compress(str));
        sc.close();
    }
    public static String compress(String str) {
        int count[] = new int[256];
        for (int i = 0; i < str.length(); i++) {
            count[str.charAt(i)]++;
        }
        String result = "";
        for (int i = 0; i < 256; i++) {
            if (count[i] > 0) {
                result += (char) i;
                result += count[i];
            }
        }
        return result;
    }
}
