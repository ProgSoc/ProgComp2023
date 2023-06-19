import java.lang.Math;
import java.util.Scanner;
import java.util.Arrays;

public class solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        printSpiral(s);
    }

    public static void printSpiral(String s) {
        int n = (int) Math.ceil(Math.sqrt(s.length()));

        // Initialize the matrix
        char[][] matrix = new char[n][n];
        for (char[] row: matrix) {
            Arrays.fill(row, ' ');
        }

        // Calculate the boundaries
        int top = 0;
        int bottom = n - 1;
        int left = 0;
        int right = n - 1;

        // Initialize the string index
        int index = 0;

        while (true) {
            // Print the top row
            for (int i = left; i <= right; i++) {
                if (index >= s.length()) {
                    break;
                }
                matrix[top][i] = s.charAt(index);
                index++;
            }
            top++;
            if (!(top <= bottom)) {
                break;
            }

            // Print the right column
            for (int i = top; i <= bottom; i++) {
                if (index >= s.length()) {
                    break;
                }
                matrix[i][right] = s.charAt(index);
                index++;
            }
            right--;
            if (!(left <= right)) {
                break;
            }

            // Print the bottom row
            for (int i = right; i >= left; i--) {
                if (index >= s.length()) {
                    break;
                }
                matrix[bottom][i] = s.charAt(index);
                index++;
            }
            bottom--;
            if (!(top <= bottom)) {
                break;
            }

            // Print the left column
            for (int i = bottom; i >= top; i--) {
                if (index >= s.length()) {
                    break;
                }
                matrix[i][left] = s.charAt(index);
                index++;
            }
            left++;
            if (!(left <= right)) {
                break;
            }

            if (index >= s.length()) {
                break;
            }
        }

        // Print the matrix
        for (char[] row : matrix) {
            boolean first = true;
            for (char c : row) {
                if (first) {
                    first = false;
                } else {
                    System.out.print(" ");
                }
                System.out.print(c);
            }
            System.out.println();
        }
    }
}