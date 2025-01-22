import java.util.HashMap;
import java.util.Scanner;

public class highestOccuringCharacter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(highestOccurance2(str));
        sc.close();
    }
    // This function has O(n) time complexity using array
    public static char highestOccurance(String str) {
        int count[] = new int[256];
        for (int i = 0; i < str.length(); i++) {
            //increment the count of the character at the index of the character
            count[str.charAt(i)]++;
        }
        int max = -1;
        char result = ' ';
        //find the character with the highest count
        for (int i = 0; i < str.length(); i++) {
            if (max < count[str.charAt(i)]) {
                max = count[str.charAt(i)];
                result = str.charAt(i);
            }
        }
        return result;
    }
    // This function has O(n) time complexity using HashMap
    public static char highestOccurance2(String str) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        int max = -1;
        char result = ' ';
        for (char ch : map.keySet()) {
            if (max < map.get(ch)) {
                max = map.get(ch);
                result = ch;
            }
        }
        return result;
    }
}
