#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

void printSpiral(std::string s) {
    int n = std::ceil(std::sqrt(s.length()));

    // Initialize the matrix
    std::vector<std::vector<char>> matrix(n, std::vector<char>(n, ' '));

    // Calculate the boundaries
    int top = 0;
    int bottom = n - 1;
    int left = 0;
    int right = n - 1;

    // Initialize the string index
    int index = 0;

    while (true) {
        // Print the top row
        for (int i = left; i <= right; i++) {
            if (index >= s.length()) {
                break;
            }
            matrix[top][i] = s.at(index);
            index++;
        }
        top++;
        if (!(top <= bottom)) {
            break;
        }

        // Print the right column
        for (int i = top; i <= bottom; i++) {
            if (index >= s.length()) {
                break;
            }
            matrix[i][right] = s.at(index);
            index++;
        }
        right--;
        if (!(left <= right)) {
            break;
        }

        // Print the bottom row
        for (int i = right; i >= left; i--) {
            if (index >= s.length()) {
                break;
            }
            matrix[bottom][i] = s.at(index);
            index++;
        }
        bottom--;
        if (!(top <= bottom)) {
            break;
        }

        // Print the left column
        for (int i = bottom; i >= top; i--) {
            if (index >= s.length()) {
                break;
            }
            matrix[i][left] = s.at(index);
            index++;
        }
        left++;
        if (!(left <= right)) {
            break;
        }

        if (index >= s.length()) {
            break;
        }
    }

    // Print the matrix
    for (std::vector<char>& row : matrix) {
        bool first = true;
        for (char c : row) {
            if (!first) {
                std::cout << " ";
            }
            std::cout << c;
            first = false;
        }
        std::cout << "\n";
    }
}

int main() {
    std::string s;
    std::getline(std::cin, s);
    printSpiral(s);
    return 0;
}