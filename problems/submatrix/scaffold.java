import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class solution {
    public static void binarySubmatrix(int[][] image) {
        // Your solution goes here
    }

    public static void main(String[] args) {
        int[][] matrix = parseMatrix();
        binarySubmatrix(matrix);
    }

    public static int[][] parseMatrix() {
        Scanner scanner = new Scanner(System.in);
        int size = scanner.nextInt();
        scanner.nextLine();

        List<int[]> matrixList = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            String line = scanner.nextLine();
            if (line.isEmpty()) {
                break;
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
}