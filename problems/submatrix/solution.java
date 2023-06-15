import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class solution {
    public static void main(String[] args) {
        int[][] matrix = parseMatrix();
        int[] answer = findLargestSquareSubmatrix(matrix);
        System.out.println(answer[2]);
        System.out.println(answer[0] + " " + answer[1]);
    }

    public static int[][] parseMatrix() {
        Scanner scanner = new Scanner(System.in);
        int size = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character

        List<int[]> matrixList = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            String line = scanner.nextLine();
            if (line.isEmpty()) {
                break; // Stop reading if an empty line is encountered
            }

            String[] elements = line.split(" ");
            int[] row = new int[elements.length];

            for (int j = 0; j < elements.length; j++) {
                row[j] = Integer.parseInt(elements[j]);
            }

            matrixList.add(row);
        }

        int[][] matrix = new int[matrixList.size()][];
        for (int i = 0; i < matrixList.size(); i++) {
            matrix[i] = matrixList.get(i);
        }

        return matrix;
    }

    public static int[] findLargestSquareSubmatrix(int[][] matrix) {
        int rows = matrix.length;
        if (rows == 0) {
            return new int[]{0, 0, 0};
        }
        int cols = matrix[0].length;

        int[][] dp = new int[rows + 1][cols + 1];
        int maxSize = 0;
        int maxPosI = 0;
        int maxPosJ = 0;

        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                if (matrix[i - 1][j - 1] == 1) {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i][j - 1], dp[i - 1][j])) + 1;
                    if (maxSize < dp[i][j]) {
                        maxSize = dp[i][j];
                        maxPosI = i;
                        maxPosJ = j;
                    }
                }
            }
        }

        int iPos = maxPosI - maxSize;
        int jPos = maxPosJ - maxSize;
        return new int[]{iPos, jPos, maxSize};
    }
}