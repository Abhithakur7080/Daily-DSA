import java.util.Scanner;

public class reverseStringWordWise {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(reverse2(str));
        sc.close();
    }
    public static  String reverse(String str){
        String result = "";
        int index = str.length() - 1;
        while(index >= 0){
            int end = index;
            //find the start of the word
            while(index >= 0 && str.charAt(index) != ' '){
                index--;
            }
            //add the word to the result from index to end
            result += str.substring(index + 1, end + 1) + " ";
            index--;
        }
        return result;
    }
    public static String reverse2(String str) {
        //converted into array
        String[] strArr = str.trim().split(" ");
        //reversed the array
        StringIO.collection.reverse(0, strArr.length - 1, strArr);
        //return the array as string
        return String.join(" ", strArr);
    }
}
