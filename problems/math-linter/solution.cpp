#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <algorithm>

using namespace std;

enum Expects
{
    EXPRESSION,
    OPERATOR,
    MINUS,
    CLOSING_BRACKET
};

vector<Expects> BEGIN_EXPR = {EXPRESSION, MINUS};
vector<Expects> AFTER_EXPR = {OPERATOR, CLOSING_BRACKET};
vector<Expects> AFTER_OPERATOR = {EXPRESSION};
vector<Expects> AFTER_MINUS = {EXPRESSION};
vector<Expects> AFTER_CLOSING_BRACKET = {OPERATOR, CLOSING_BRACKET};

bool validateNumber(string token)
{
    return regex_match(token, regex("^\\d+(\\.\\d+)?$"));
}

bool validateOperator(string token)
{
    return token == "+" || token == "-" || token == "*" || token == "/";
}

bool validateExpression(vector<string> tokens)
{
    int parensDeep = 0;
    vector<Expects> expects = BEGIN_EXPR;

    for (string token : tokens)
    {
        bool valid = false;
        for (Expects exp : expects)
        {
            if (valid)
            {
                break;
            }

            switch (exp)
            {
            case EXPRESSION:
                if (validateNumber(token))
                {
                    expects = AFTER_EXPR;
                    valid = true;
                }
                else if (token == "(")
                {
                    parensDeep++;
                    expects = BEGIN_EXPR;
                    valid = true;
                }
                break;
            case OPERATOR:
                if (validateOperator(token))
                {
                    expects = AFTER_OPERATOR;
                    valid = true;
                }
                break;
            case MINUS:
                if (token == "-")
                {
                    expects = AFTER_MINUS;
                    valid = true;
                }
                break;
            case CLOSING_BRACKET:
                if (token == ")")
                {
                    parensDeep--;
                    expects = AFTER_CLOSING_BRACKET;
                    valid = true;
                }
                break;
            }
        }

        if (!valid)
        {
            return false;
        }

        if (parensDeep < 0)
        {
            return false;
        }
    }

    bool validParens = parensDeep == 0;
    bool validExpressionEnd = (expects == AFTER_EXPR || expects == AFTER_CLOSING_BRACKET);

    return validParens && validExpressionEnd;
}

int main() {
    string input;
    getline(cin, input);
    vector<string> tokens;
    stringstream ss(input);
    string temp;
    while(getline(ss, temp, ' ')) {
        tokens.push_back(temp);
    }
    bool isValid = validateExpression(tokens);
    cout << (isValid ? "true" : "false") << endl;
    return 0;
}