#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

string solveMaze(vector<vector<bool>> &maze)
{
    // Your solution goes here
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