#include <iostream>
#include <vector>
using namespace std;

pair<pair<int, int>, int> findLargestSquareSubMatrix(vector<vector<int>>& matrix) {
    // Your solution goes here
    return make_pair(make_pair(x, y), max_size);
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