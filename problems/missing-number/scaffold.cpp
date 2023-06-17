#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int findMissingNumber(const vector<int> &arr)
{
    // Your solution goes here
    return missingNumber;
}

int main()
{
    string input;
    getline(cin, input);

    vector<int> array;
    stringstream ss(input);
    string num;
    while (getline(ss, num, ','))
    {
        array.push_back(stoi(num));
    }

    int missingNumber = findMissingNumber(array);
    cout << missingNumber << endl;

    return 0;
}