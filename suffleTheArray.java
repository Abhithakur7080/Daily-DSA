public class suffleTheArray{
    public static void main(String[] args) {
        int array[] = ArraysIO.input.takeInput_1d();
        suffle(array);
        ArraysIO.output.print(array);
    }
    public static void suffle(int array[]){
        for(int i = 0; i < array.length; i++){
            int randomIndex = (int)(Math.random() * array.length);
            int temp = array[i];
            array[i] = array[randomIndex];
            array[randomIndex] = temp;
        }
    }
}