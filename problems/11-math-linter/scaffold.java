import java.util.*;
import java.util.regex.Pattern;

public class solution {
    private static boolean validateExpression(String[] tokens) {
        // Your solution goes here
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] tokens = scanner.nextLine().split(" ");
        boolean isValid = validateExpression(tokens);
        System.out.println(isValid ? "true" : "false");
    }
}