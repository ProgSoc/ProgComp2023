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
        double x1 = p1.x;
        double y1 = p1.y;
        double r1 = p1.distance;
        double x2 = p2.x;
        double y2 = p2.y;
        double r2 = p2.distance;
        double x3 = p3.x;
        double y3 = p3.y;
        double r3 = p3.distance;

        double A = 2 * (x2 - x1);
        double B = 2 * (y2 - y1);
        double C = r1 * r1 - r2 * r2 - x1 * x1 + x2 * x2 - y1 * y1 + y2 * y2;
        double D = 2 * (x3 - x1);
        double E = 2 * (y3 - y1);
        double F = r1 * r1 - r3 * r3 - x1 * x1 + x3 * x3 - y1 * y1 + y3 * y3;

        double x = (C * E - F * B) / (E * A - B * D);
        double y = (C * D - A * F) / (B * D - A * E);

        return new Point(x, y);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Coordinate p1 = readCoordinate(scanner);
        Coordinate p2 = readCoordinate(scanner);
        Coordinate p3 = readCoordinate(scanner);

        Point result = trilaterate(p1, p2, p3);

        System.out.printf("%.2f %.2f%n", result.x, result.y);
    }

    private static Coordinate readCoordinate(Scanner scanner) {
        double x = scanner.nextDouble();
        double y = scanner.nextDouble();
        double distance = scanner.nextDouble();
        return new Coordinate(x, y, distance);
    }
}