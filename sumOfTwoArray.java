public class sumOfTwoArray {
    public static void main(String[] args) {
        int array1[] = ArraysIO.input.takeInput_1d();
        int array2[] = ArraysIO.input.takeInput_1d();
        int result[] = sumArr(array1, array2);
        ArraysIO.output.print(result);

    }
    public static int[] sumArr(int arr1[], int arr2[]){
        int m = arr1.length-1;
        int n = arr2.length-1;
        int c = 0;

        int maxLength = Math.max(arr1.length, arr2.length);
        int[] output = new int[maxLength + 1];
        int x = maxLength;

        while (m >= 0 && n >= 0) {
            int sum = arr1[m] + arr2[n] + c;
            output[x] = sum % 10;
            c = sum / 10;
            m--;
            n--;
            x--;
        }
        while (m >= 0) {
            int sum = arr1[m] + c;
            output[x] = sum % 10;
            c = sum / 10;
            m--;
            x--;
        }
        while (n >= 0) {
            int sum = arr2[n] + c;
            output[x] = sum % 10;
            c = sum / 10;
            n--;
            x--;
        }
        output[x] = c;
        if (output[0] == 0) {
            int[] trimmedOutput = new int[output.length - 1];
            System.arraycopy(output, 1, trimmedOutput, 0, trimmedOutput.length);
            return trimmedOutput;
        }
        return output;

    }
}
