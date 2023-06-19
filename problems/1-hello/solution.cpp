#include <iostream>
#include <string>
#include <cctype>

std::string getGreeting(const std::string &name)
{
    return "Hello " + name + "!";
}

int main()
{
    std::string name;
    std::getline(std::cin, name);
    std::cout << getGreeting(name) << std::endl;
    return 0;
}