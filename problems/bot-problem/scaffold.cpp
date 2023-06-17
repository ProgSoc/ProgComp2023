#include <iostream>
#include <vector>

using namespace std;

bool isSpamBot(string username)
{
    // Your solution goes here
}

int main()
{
    int usernameCount;
    cin >> usernameCount;

    vector<string> usernames(usernameCount);
    for (int i = 0; i < usernameCount; i++)
    {
        cin >> usernames[i];
    }

    for (const string &username : usernames)
    {
        if (isSpamBot(username))
        {
            cout << username << endl;
        }
    }

    return 0;
}