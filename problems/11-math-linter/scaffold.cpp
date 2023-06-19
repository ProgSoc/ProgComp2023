#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <algorithm>

using namespace std;

bool validateExpression(vector<string> tokens)
{
    // Your solution goes here
}

int main()
{
    string input;
    getline(cin, input);
    vector<string> tokens;
    stringstream ss(input);
    string temp;
    while (getline(ss, temp, ' '))
    {
        tokens.push_back(temp);
    }
    bool isValid = validateExpression(tokens);
    cout << (isValid ? "true" : "false") << endl;
    return 0;
}