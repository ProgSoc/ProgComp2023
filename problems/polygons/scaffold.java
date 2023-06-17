import java.util.*;


class Point {
    double x, y;
    Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
}

public class solution {
    static List<Point> polygonIntersection(List<Point> poly1, List<Point> poly2) {
        // Write your solution here
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        List<Point> poly1 = readPoly(in);
        List<Point> poly2 = readPoly(in);
        List<Point> intersection = polygonIntersection(poly1, poly2);
        System.out.println(polygonArea(intersection));
    }

    static double polygonArea(List<Point> points) {
        double area = 0;
        int n = points.size();
        for (int i = 0; i < n; i++) {
            Point current = points.get(i);
            Point next = points.get((i+1)%n);
            area += current.x * next.y - next.x * current.y;
        }
        return Math.abs(area) / 2;
    }

    static List<Point> readPoly(Scanner in) {
        String[] pointsStr = in.nextLine().split(" ");
        List<Point> points = new ArrayList<>();
        for (String pointStr : pointsStr) {
            String[] coordinates = pointStr.split(",");
            double x = Double.parseDouble(coordinates[0]);
            double y = Double.parseDouble(coordinates[1]);
            points.add(new Point(x, y));
        }
        return points;
    }
}