import re


def validate_number(token: str) -> bool:
    return re.match(r"^\d+(\.\d+)?$", token) is not None


def validate_operator(token: str) -> bool:
    return token in ["+", "-", "*", "/"]


class Expects:
    EXPRESSION = 0
    OPERATOR = 1
    MINUS = 2
    CLOSING_BRACKET = 3


BEGIN_EXPR = [Expects.EXPRESSION, Expects.MINUS]
AFTER_EXPR = [Expects.OPERATOR, Expects.CLOSING_BRACKET]
AFTER_OPERATOR = [Expects.EXPRESSION]
AFTER_MINUS = [Expects.EXPRESSION]
AFTER_CLOSING_BRACKET = [Expects.OPERATOR, Expects.CLOSING_BRACKET]


def validate_expression(tokens: list[str]) -> bool:
    parens_deep = 0
    expects = BEGIN_EXPR

    for token in tokens:
        valid = False
        for exp in expects:
            if valid:
                break

            if exp == Expects.EXPRESSION:
                if validate_number(token):
                    expects = AFTER_EXPR
                    valid = True
                elif token == "(":
                    parens_deep += 1
                    expects = BEGIN_EXPR
                    valid = True
            elif exp == Expects.OPERATOR:
                if validate_operator(token):
                    expects = AFTER_OPERATOR
                    valid = True
            elif exp == Expects.MINUS:
                if token == "-":
                    expects = AFTER_MINUS
                    valid = True
            elif exp == Expects.CLOSING_BRACKET:
                if token == ")":
                    parens_deep -= 1
                    expects = AFTER_CLOSING_BRACKET
                    valid = True

        if not valid:
            return False

        if parens_deep < 0:
            return False

    valid_parens = parens_deep == 0
    valid_expression_end = expects == AFTER_EXPR or expects == AFTER_CLOSING_BRACKET

    return valid_parens and valid_expression_end


tokens = input().split(" ")
is_valid = validate_expression(tokens)
if is_valid:
    print("true")
else:
    print("false")
