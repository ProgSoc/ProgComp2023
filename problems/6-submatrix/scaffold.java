import java.util.Scanner;

public class solution {
    public static int[][] findLargestSquareSubMatrix(int[][] matrix) {
        // Your solution goes here
        return new int[][]{{x, y}, {max_size}};
    }

    public static void main(String[] args) {
        int[][] matrix = parseMatrix();
        int[][] answer = findLargestSquareSubMatrix(matrix);
        System.out.println(answer[1][0]);
        System.out.println(answer[0][0] + " " + answer[0][1]);
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