#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

vector<vector<int>> parseMatrix() {
    int size;
    cin >> size;
    cin.ignore(); // Ignore the newline character

    vector<vector<int>> matrix;

    for (int i = 0; i < size; i++) {
        string line;
        getline(cin, line);

        if (line.empty()) {
            break;
        }

        stringstream ss(line);
        vector<int> row;

        int num;
        while (ss >> num) {
            row.push_back(num);
        }

        matrix.push_back(row);
    }

    return matrix;
}

void binarySubmatrix(vector<vector<int>>& image) {
    // Your solution goes here
}

int main() {
    vector<vector<int>> matrix = parseMatrix();
    binarySubmatrix(matrix);

    return 0;
}