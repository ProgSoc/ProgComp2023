#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

pair<pair<int, int>, int> findLargestSquareSubmatrix(const vector<vector<int>>& matrix) {
    int rows = matrix.size();
    if (rows == 0) {
        return make_pair(make_pair(0, 0), 0);
    }
    int cols = matrix[0].size();

    vector<vector<int>> dp(rows + 1, vector<int>(cols + 1, 0));
    int maxSize = 0;
    int maxPosI = 0;
    int maxPosJ = 0;

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= cols; j++) {
            if (matrix[i - 1][j - 1] == 1) {
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1;
                if (maxSize < dp[i][j]) {
                    maxSize = dp[i][j];
                    maxPosI = i;
                    maxPosJ = j;
                }
            }
        }
    }

    int iPos = maxPosI - maxSize;
    int jPos = maxPosJ - maxSize;
    return make_pair(make_pair(iPos, jPos), maxSize);
}

vector<vector<int>> parseMatrix() {
    int size;
    cin >> size;
    cin.ignore(); // Ignore the newline character

    vector<vector<int>> matrix;

    for (int i = 0; i < size; i++) {
        string line;
        getline(cin, line);

        if (line.empty()) {
            break; // Stop reading if an empty line is encountered
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

int main() {
    vector<vector<int>> matrix = parseMatrix();
    pair<pair<int, int>, int> answer = findLargestSquareSubmatrix(matrix);
    cout << answer.second << endl;
    cout << answer.first.first << " " << answer.first.second << endl;

    return 0;
}