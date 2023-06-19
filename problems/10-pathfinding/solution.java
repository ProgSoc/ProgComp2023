import java.util.*;

public class solution {
    private static class Position {
        int x, y;
        Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Position position = (Position) o;
            return x == position.x &&
                    y == position.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    private static class Node {
        Position position;
        String path;
        Node(Position position, String path) {
            this.position = position;
            this.path = path;
        }
    }

    private static String solveMaze(boolean[][] maze) {
        int rows = maze.length, cols = maze[0].length;
        Position start = new Position(0, 1);  // start position
        Position goal = new Position(rows - 1, cols - 2);  // goal position

        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(start, ""));
        Set<Position> visited = new HashSet<>();
        visited.add(start);

        while (!queue.isEmpty()) {
            Node node = queue.removeFirst();
            Position pos = node.position;
            String path = node.path;

            int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            char[] directionLabels = {'U', 'D', 'L', 'R'};
            for (int i = 0; i < 4; i++) {
                int nx = pos.x + directions[i][0];
                int ny = pos.y + directions[i][1];
                Position newPos = new Position(nx, ny);

                if (0 <= nx && nx < rows && 0 <= ny && ny < cols && !maze[nx][ny]) {
                    if (newPos.equals(goal)) {
                        return path + directionLabels[i];
                    } else if (!visited.contains(newPos)) {
                        queue.addLast(new Node(newPos, path + directionLabels[i]));
                        visited.add(newPos);
                    }
                }
            }
        }

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