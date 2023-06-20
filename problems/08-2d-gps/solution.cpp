#include <iostream>

struct Coordinate
{
    double x;
    double y;
    double distance;

    Coordinate(double x, double y, double distance) : x(x), y(y), distance(distance) {}
};

struct Point
{
    double x;
    double y;

    Point(double x, double y) : x(x), y(y) {}
};

Point trilaterate(const Coordinate &p1, const Coordinate &p2, const Coordinate &p3)
{
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

    return Point(x, y);
}

Coordinate readCoordinate()
{
    double x, y, distance;
    std::cin >> x >> y >> distance;
    return Coordinate(x, y, distance);
}

int main()
{
    Coordinate p1 = readCoordinate();
    Coordinate p2 = readCoordinate();
    Coordinate p3 = readCoordinate();

    Point result = trilaterate(p1, p2, p3);

    std::cout << std::fixed;
    std::cout << (int)result.x << " " << (int)result.y << std::endl;

    return 0;
}
