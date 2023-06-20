#include <iostream>
#include <vector>
using namespace std;

pair<pair<int, int>, int> findLargestSquareSubMatrix(vector<vector<int>>& matrix) {
    int rows = matrix.size();
    if (rows == 0) {
        return make_pair(make_pair(0, 0), 0);
    }

    int cols = matrix[0].size();

    vector<vector<int>> dp(rows + 1, vector<int>(cols + 1, 0));
    int max_size = 0;
    int max_pos_i = 0;
    int max_pos_j = 0;

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= cols; j++) {
            if (matrix[i - 1][j - 1] == 1) {
                dp[i][j] = min(min(dp[i - 1][j - 1], dp[i][j - 1]), dp[i - 1][j]) + 1;
                if (max_size < dp[i][j]) {
                    max_size = dp[i][j];
                    max_pos_i = i;
                    max_pos_j = j;
                }
            }
        }
    }

    int i_pos = max_pos_i - max_size;
    int j_pos = max_pos_j - max_size;
    return make_pair(make_pair(i_pos, j_pos), max_size);
}

vector<vector<int>> parseMatrix() {
    int size;
    cin >> size;
    vector<vector<int>> matrix(size, vector<int>(size));

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            cin >> matrix[i][j];
        }
    }

    return matrix;
}

int main() {
    vector<vector<int>> matrix = parseMatrix();
    pair<pair<int, int>, int> answer = findLargestSquareSubMatrix(matrix);
    cout << answer.second << endl;
    cout << answer.first.first << " " << answer.first.second << endl;
    return 0;
}