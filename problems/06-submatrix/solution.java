import java.util.Scanner;

public class solution {
    public static void main(String[] args) {
        int[][] matrix = parseMatrix();
        int[][] answer = findLargestSquareSubMatrix(matrix);
        System.out.println(answer[1][0]);
        System.out.println(answer[0][0] + " " + answer[0][1]);
    }

    public static int[][] findLargestSquareSubMatrix(int[][] matrix) {
        int rows = matrix.length;
        if (rows == 0) {
            return new int[][]{{0, 0}, {0}};
        }

        int cols = matrix[0].length;

        int[][] dp = new int[rows + 1][cols + 1];
        int max_size = 0;
        int max_pos_i = 0;
        int max_pos_j = 0;

        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                if (matrix[i - 1][j - 1] == 1) {
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j - 1], dp[i][j - 1]), dp[i - 1][j]) + 1;
                    if (max_size < dp[i][j]) {
                        max_size = dp[i][j];
                        max_pos_i = i;
                        max_pos_j = j;
                    }
                }
            }
        }

        int i_pos = max_pos_i - max_size;
        int j_pos = max_pos_j - max_size;
        return new int[][]{{i_pos, j_pos}, {max_size}};
    }

    public static int[][] parseMatrix() {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        sc.nextLine(); // Consume newline character
        int[][] matrix = new int[size][size];

        for (int i = 0; i < size; i++) {
            String[] line = sc.nextLine().split(" ");
            for (int j = 0; j < size; j++) {
                matrix[i][j] = Integer.parseInt(line[j]);
            }
        }

        return matrix;
    }
}