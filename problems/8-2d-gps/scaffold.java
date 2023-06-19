import java.util.Scanner;

class Coordinate {
    public double x;
    public double y;
    public double distance;

    public Coordinate(double x, double y, double distance) {
        this.x = x;
        this.y = y;
        this.distance = distance;
    }
}

class Point {
    public double x;
    public double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
}

public class solution {
    private static Point trilaterate(Coordinate p1, Coordinate p2, Coordinate p3) {
        // Your solution goes here
        return new Point(x, y);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Coordinate p1 = readCoordinate(scanner);
        Coordinate p2 = readCoordinate(scanner);
        Coordinate p3 = readCoordinate(scanner);

        Point result = trilaterate(p1, p2, p3);

        System.out.println((int)result.x + " " + (int)result.y);
    }

    private static Coordinate readCoordinate(Scanner scanner) {
        double x = scanner.nextDouble();
        double y = scanner.nextDouble();
        double distance = scanner.nextDouble();
        return new Coordinate(x, y, distance);
    }
}