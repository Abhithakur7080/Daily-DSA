import java.util.Scanner;

public class isPalindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(palindrome(n));
        sc.close();
    }

    public static boolean palindrome(int n) {
        // This function has O(1) time complexity having input range 0 to 1000 only
        // if constraints: 0 <= n <= 1000
        if (n < 0) {
            return false;
        } else if (n <= 10) {
            return true;
        } else if ((10 < n && n <= 100) && n % 10 == n / 10) {
            return true;
        } else if (100 < n && n <= 1000 && n % 10 == n / 100) {
            return true;
        } else {
            return false;
        }
    }
}
