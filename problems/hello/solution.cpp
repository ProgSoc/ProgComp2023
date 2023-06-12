#include <iostream>
#include <string>
#include <cctype>

std::string getGreeting(const std::string& name) {
    std::string capitalizedName = "";
    if (!name.empty()) {
        capitalizedName += std::toupper(name[0]);
        for (int i = 1; i < name.size(); ++i) {
            capitalizedName += std::tolower(name[i]);
        }
    }
    return "Hello " + capitalizedName + "!";
}

int main() {
    std::string name;
    std::getline(std::cin, name);
    std::cout << getGreeting(name) << std::endl;
    return 0;
}