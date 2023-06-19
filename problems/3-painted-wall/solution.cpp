#include <iostream>
#include <string>
using namespace std;

int brokenSequence(string wall)
{
    int count = 0;

    for (int i = 0; i < wall.length() - 1; i++)
    {
        string pair = wall.substr(i, 2);

        if (pair == "RG" || pair == "GB" || pair == "BR")
        {
            continue;
        }
        else
        {
            count++;
        }
    }

    return count;
}

int main()
{
    string text;
    getline(cin, text);
    cout << brokenSequence(text) << endl;
    return 0;
}