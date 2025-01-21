import java.util.Scanner;

public class countWords {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(count2(str));
        sc.close();
    }
    public static int count(String str){
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if(str.charAt(i) == ' '){
                count++;
            }
        }
        return count+1;
    }
    public static int count2(String str){
        return str.split(str, ' ').length;
    }
}
