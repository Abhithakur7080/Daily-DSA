public class mergeTwoSortedArray {
    public static void main(String[] args) {
        int array1[] = ArraysIO.input.takeInput_1d();
        int array2[] = ArraysIO.input.takeInput_1d();
        int solution[] = merge(array1, array2);
        ArraysIO.output.print(solution);
    }
    public static int[] merge(int arr1[], int arr2[]){
        int m = arr1.length;
        int n = arr2.length;
        int result[] = new int[m+n];
        int i=0, j=0, k=0;
        while (i<m && j<n) {
            if(arr1[i] < arr2[j]){
                result[k] = arr1[i];
                i++;
                k++;
            } else {
                result[k] = arr2[j];
                j++;
                k++;
            }
        }
        while (i<m) {
            result[k] = arr1[i];
            i++;
            k++;
        }
        while (j<n) {
            result[k] = arr2[j];
            j++;
            k++;
        }
        return result;
    }
}
