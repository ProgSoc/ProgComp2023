import java.util.*;
import java.util.regex.Pattern;

public class solution {
    private enum Expects {
        EXPRESSION, OPERATOR, MINUS, CLOSING_BRACKET
    }

    private static final List<Expects> BEGIN_EXPR = Arrays.asList(Expects.EXPRESSION, Expects.MINUS);
    private static final List<Expects> AFTER_EXPR = Arrays.asList(Expects.OPERATOR, Expects.CLOSING_BRACKET);
    private static final List<Expects> AFTER_OPERATOR = Collections.singletonList(Expects.EXPRESSION);
    private static final List<Expects> AFTER_MINUS = Collections.singletonList(Expects.EXPRESSION);
    private static final List<Expects> AFTER_CLOSING_BRACKET = Arrays.asList(Expects.OPERATOR, Expects.CLOSING_BRACKET);

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] tokens = scanner.nextLine().split(" ");
        boolean isValid = validateExpression(tokens);
        System.out.println(isValid ? "true" : "false");
    }

    private static boolean validateNumber(String token) {
        return Pattern.matches("^\\d+(\\.\\d+)?$", token);
    }

    private static boolean validateOperator(String token) {
        return Arrays.asList("+", "-", "*", "/").contains(token);
    }

    private static boolean validateExpression(String[] tokens) {
        int parensDeep = 0;
        List<Expects> expects = new ArrayList<>(BEGIN_EXPR);

        for (String token : tokens) {
            boolean valid = false;
            for (Expects exp : expects) {
                if (valid) {
                    break;
                }

                switch (exp) {
                    case EXPRESSION:
                        if (validateNumber(token)) {
                            expects = new ArrayList<>(AFTER_EXPR);
                            valid = true;
                        } else if (token.equals("(")) {
                            parensDeep++;
                            expects = new ArrayList<>(BEGIN_EXPR);
                            valid = true;
                        }
                        break;
                    case OPERATOR:
                        if (validateOperator(token)) {
                            expects = new ArrayList<>(AFTER_OPERATOR);
                            valid = true;
                        }
                        break;
                    case MINUS:
                        if (token.equals("-")) {
                            expects = new ArrayList<>(AFTER_MINUS);
                            valid = true;
                        }
                        break;
                    case CLOSING_BRACKET:
                        if (token.equals(")")) {
                            parensDeep--;
                            expects = new ArrayList<>(AFTER_CLOSING_BRACKET);
                            valid = true;
                        }
                        break;
                }
            }

            if (!valid) {
                return false;
            }

            if (parensDeep < 0) {
                return false;
            }
        }

        boolean validParens = parensDeep == 0;
        boolean validExpressionEnd = expects.equals(AFTER_EXPR) || expects.equals(AFTER_CLOSING_BRACKET);

        return validParens && validExpressionEnd;
    }
}