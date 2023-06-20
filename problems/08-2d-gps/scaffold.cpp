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
    // Your solution goes here
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
