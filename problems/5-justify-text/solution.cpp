#include <iostream>
#include <vector>
#include <sstream>

std::string addWord(std::string line, std::string word)
{
    if (line.empty())
    {
        return word;
    }
    return line + ' ' + word;
}

std::string textJustification(int max_len, std::string text)
{
    std::istringstream iss(text);
    std::vector<std::string> words;
    std::vector<std::string> lines;
    std::string word;
    std::string currentLine = "";

    while (iss >> word)
    {
        words.push_back(word);
    }

    for (std::string word : words)
    {
        if (word.length() <= max_len)
        {
            std::string added = addWord(currentLine, word);
            if (added.length() <= max_len)
            {
                currentLine = added;
            }
            else
            {
                lines.push_back(currentLine);
                currentLine = word;
            }
        }
        else
        {
            while (word.length() > max_len)
            {
                if (!currentLine.empty())
                {
                    lines.push_back(currentLine);
                    currentLine = "";
                }
                lines.push_back(word.substr(0, max_len - 1) + '-');
                word = word.substr(max_len - 1);
            }
            currentLine = word;
        }
    }
    lines.push_back(currentLine); // appending the last line

    std::string result;
    for (std::string line : lines)
    {
        result += line + '\n';
    }
    return result;
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