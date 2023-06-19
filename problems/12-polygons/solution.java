import java.util.*;


class Point {
    double x, y;
    Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
}

class Intersection {
    Point point;
    int index1, index2;
    boolean entering;

    Intersection(Point point, int index1, int index2, boolean entering) {
        this.point = point;
        this.index1 = index1;
        this.index2 = index2;
        this.entering = entering;
    }
}

public class solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        List<Point> poly1 = readPoly(in);
        List<Point> poly2 = readPoly(in);
        List<Point> intersection = polygonIntersection(poly1, poly2);
        System.out.println(polygonArea(intersection));
    }

    static Point segmentIntersection(Point[] segment1, Point[] segment2) {
        Point xdiff = new Point(segment1[0].x - segment1[1].x, segment2[0].x - segment2[1].x);
        Point ydiff = new Point(segment1[0].y - segment1[1].y, segment2[0].y - segment2[1].y);

        double div = det(xdiff, ydiff);
        if (div == 0) {
            return null;  // Lines don't intersect
        }

        Point d = new Point(det(segment1[0], segment1[1]), det(segment2[0], segment2[1]));
        double x = det(d, xdiff) / div;
        double y = det(d, ydiff) / div;

        if (Math.min(segment1[0].x, segment1[1].x) <= x && x <= Math.max(segment1[0].x, segment1[1].x) &&
            Math.min(segment1[0].y, segment1[1].y) <= y && y <= Math.max(segment1[0].y, segment1[1].y) &&
            Math.min(segment2[0].x, segment2[1].x) <= x && x <= Math.max(segment2[0].x, segment2[1].x) &&
            Math.min(segment2[0].y, segment2[1].y) <= y && y <= Math.max(segment2[0].y, segment2[1].y)) {
            return new Point(x, y);
        }
        return null;
    }

    static double det(Point a, Point b) {
        return a.x * b.y - a.y * b.x;
    }

    static double crossProduct(Point A, Point B, Point C) {
        Point AB = new Point(B.x - A.x, B.y - A.y);
        Point AC = new Point(C.x - A.x, C.y - A.y);
        return AB.x * AC.y - AB.y * AC.x;
    }

    static boolean isExiting(Point A, Point B, Point C) {
        return crossProduct(A, B, C) < 0;
    }

    static List<Point> getPolySegment(List<Point> poly, int start, int end) {
        List<Point> segment = new ArrayList<>();
        if (end <= start) {
            segment.addAll(poly.subList(start, poly.size()));
            segment.addAll(poly.subList(0, end));
        } else {
            segment.addAll(poly.subList(start, end));
        }
        return segment;
    }

    static List<Point> polygonIntersection(List<Point> poly1, List<Point> poly2) {
        List<Intersection> intersections = new ArrayList<>();

        for (int i = 0; i < poly1.size(); i++) {
            for (int j = 0; j < poly2.size(); j++) {
                Point[] seg1 = { poly1.get((i-1+poly1.size())%poly1.size()), poly1.get(i) };
                Point[] seg2 = { poly2.get((j-1+poly2.size())%poly2.size()), poly2.get(j) };
                Point intersection = segmentIntersection(seg1, seg2);
                if (intersection != null) {
                    boolean exiting = isExiting(seg1[0], seg1[1], seg2[1]);
                    intersections.add(new Intersection(intersection, i, j, !exiting));
                }
            }
        }

        Intersection enteringIntersection = null;
        Intersection exitingIntersection = null;
        for (Intersection intersection : intersections) {
            if (intersection.entering) enteringIntersection = intersection;
            else exitingIntersection = intersection;
        }

        List<Point> seg1 = getPolySegment(poly1, exitingIntersection.index1, enteringIntersection.index1);
        List<Point> seg2 = getPolySegment(poly2, enteringIntersection.index2, exitingIntersection.index2);

        List<Point> newPoly = new ArrayList<>();
        newPoly.add(enteringIntersection.point);
        newPoly.addAll(seg2);
        newPoly.add(exitingIntersection.point);
        newPoly.addAll(seg1);

        return newPoly;
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