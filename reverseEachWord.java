import java.util.Scanner;

public class reverseEachWord {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str =sc.nextLine();
        System.out.println(reverse(str));
        sc.close();
    }
    public static String reverse(String str) {
        String[] words = str.split(" ");
        for (int i = 0; i < words.length; i++) {
            String[] wordArray = words[i].split("");
            StringIO.collection.reverse(0, wordArray.length - 1, wordArray);
            words[i] = String.join("", wordArray);
        }
        return String.join(" ", words);
    }
}
