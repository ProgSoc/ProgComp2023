#include <iostream>
#include <vector>
#include <regex>

using namespace std;

bool isSpamBot(string username)
{
    regex pattern("^[A-Z][a-z]+[A-Z][a-z]+\\d{3}$");
    return regex_match(username, pattern);
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