#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

string recoverData(vector<string> lines) {
    string result;

    int lineLength = lines[0].length();
    for (int c = 0; c < lineLength; c++) {
        map<char, int> counts;
        for (string line : lines) {
            char ch = line[c];
            if (ch != ' ') {
                counts[ch] = counts[ch] + 1;
            }
        }

        if (counts.empty()) {
            result += ' ';
        } else {
            char ch = max_element(counts.begin(), counts.end(), [](const auto& a, const auto& b) {
                return a.second < b.second;
            })->first;
            result += ch;
        }
    }

    return result;
}

int main() {
    int lineCount;
    cin >> lineCount;
    cin.ignore();

    vector<string> lines;
    for (int i = 0; i < lineCount; i++) {
        string text;
        getline(cin, text);
        lines.push_back(text.substr(1, text.length() - 2));
    }

    string recovered = recoverData(lines);
    cout << recovered << endl;

    return 0;
}