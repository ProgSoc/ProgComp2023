#include <iostream>
#include <vector>
#include <sstream>

std::string textJustification(int max_len, std::string text)
{
    // Your solution goes here
    return ""
}

int main()
{
    int max_length;
    std::cin >> max_length;

    std::string line;
    std::cin.ignore();
    std::getline(std::cin, line);

    std::cout << textJustification(max_length, line);
    return 0;
}