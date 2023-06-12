#include <iostream>
#include <string>

std::string getGreeting(const std::string &name)
{
    // Write your solution here
}

int main()
{
    std::string name;
    std::getline(std::cin, name);
    std::cout << getGreeting(name) << std::endl;
    return 0;
}
