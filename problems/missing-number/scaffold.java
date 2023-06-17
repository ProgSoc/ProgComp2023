import java.util.Scanner;

public class solution {
    public static int findMissingNumber(int[] arr) {
        // Your solution goes here
        return missingNumber;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] arrayString = input.split(",");
        int[] array = new int[arrayString.length];

        for (int i = 0; i < arrayString.length; i++) {
            array[i] = Integer.parseInt(arrayString[i].trim());
        }

        int missingNumber = findMissingNumber(array);
        System.out.println(missingNumber);
    }
}