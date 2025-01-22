import java.util.Scanner;

public class allSubstring{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        String result[] = substrings(str);
        StringIO.output.print_1d(result);
        sc.close();
    }
    public static String[] substrings(String str) {
        int n = str.length();
        String result[] = new String[n * (n + 1) / 2];
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                result[index++] = str.substring(i, j);
            }
        }
        return result;
    }
}