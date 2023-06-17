import java.util.*;

public class solution {
    private static String solveMaze(boolean[][] maze) {
        // Your solution goes here
        return "";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int size = scanner.nextInt();
        scanner.nextLine();  // Consume newline left-over

        boolean[][] maze = new boolean[size][size];

        for(int i = 0; i < size; i++) {
            String line = scanner.nextLine();
            for(int j = 0; j < line.length(); j+=2) {
                maze[i][j/2] = line.charAt(j) == '#';
            }
        }

        String solved = solveMaze(maze);
        System.out.println(solved);
    }
}