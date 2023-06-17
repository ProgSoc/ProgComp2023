#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

string recoverData(vector<string> lines)
{
    // Your solution goes here
    return "";
}

int main()
{
    int lineCount;
    cin >> lineCount;
    cin.ignore();

    vector<string> lines;
    for (int i = 0; i < lineCount; i++)
    {
        string text;
        getline(cin, text);
        lines.push_back(text.substr(1, text.length() - 2));
    }

    string recovered = recoverData(lines);
    cout << recovered << endl;

    return 0;
}