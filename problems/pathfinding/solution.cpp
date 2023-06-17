#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

// Represents a position in the maze
struct Position
{
    int x, y;
    Position(int x = 0, int y = 0) : x(x), y(y) {}

    bool operator==(const Position &other) const
    {
        return x == other.x && y == other.y;
    }
};

// Hash function for Position
struct PositionHash
{
    size_t operator()(const Position &p) const
    {
        return p.x * 1812433253 + p.y;
    }
};

// Represents a node in the BFS queue
struct Node
{
    Position position;
    string path;
    Node(Position position, string path) : position(position), path(path) {}
};

string solveMaze(vector<vector<bool>> &maze)
{
    int rows = maze.size(), cols = maze[0].size();
    Position start(0, 1);              // start position
    Position goal(rows - 1, cols - 2); // goal position

    queue<Node> q;
    unordered_set<Position, PositionHash> visited;
    q.push(Node(start, ""));
    visited.insert(start);

    while (!q.empty())
    {
        Node node = q.front();
        q.pop();
        Position pos = node.position;
        string path = node.path;

        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        string directionLabels = "UDLR";
        for (int i = 0; i < 4; i++)
        {
            Position newPos(pos.x + directions[i].first, pos.y + directions[i].second);
            if (0 <= newPos.x && newPos.x < rows && 0 <= newPos.y && newPos.y < cols && !maze[newPos.x][newPos.y])
            {
                if (newPos == goal)
                {
                    return path + directionLabels[i];
                }
                else if (!visited.count(newPos))
                {
                    q.push(Node(newPos, path + directionLabels[i]));
                    visited.insert(newPos);
                }
            }
        }
    }

    return "";
}

int main()
{
    int size;
    cin >> size;

    vector<vector<bool>> maze(size, vector<bool>(size));
    string line;
    getline(cin, line); // consume the rest of the first line

    for (int i = 0; i < size; i++)
    {
        getline(cin, line);
        for (int j = 0; j < line.length(); j += 2)
        {
            maze[i][j / 2] = (line[j] == '#');
        }
    }

    string solved = solveMaze(maze);
    cout << solved << endl;

    return 0;
}