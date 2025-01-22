import java.util.Scanner;

public class removeConsecutive {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(removeDuplicates(str));
        sc.close();
    }
    public static String removeDuplicates(String str) {
        String result = "";
        //store the first character
        char prev = str.charAt(0);
        //since first character is always unique
        result += prev;
        //start from 1 index
        for (int i = 1; i < str.length(); i++) {
            //if current character is not equal to previous character
            if (str.charAt(i) != prev) {
                //then add it to result
                result += str.charAt(i);
                //and update the previous character
                prev = str.charAt(i);
            }
        }
        return result;
    }
}
