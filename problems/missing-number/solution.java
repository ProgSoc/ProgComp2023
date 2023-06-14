import java.util.Scanner;

public class solution {
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

    public static int findMissingNumber(int[] arr) {
        int n = arr.length + 1;
        int totalSum = (n * (n + 1)) / 2;

        int arraySum = 0;
        for (int num : arr) {
            arraySum += num;
        }

        int missingNumber = totalSum - arraySum;
        return missingNumber;
    }
}