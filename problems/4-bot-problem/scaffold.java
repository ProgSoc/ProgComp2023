import java.util.Scanner;
import java.util.regex.Pattern;

public class solution {
    private static boolean isSpamBot(String username) {
        // Write your solution here
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int usernameCount = Integer.parseInt(scanner.nextLine());

        String[] usernames = new String[usernameCount];
        for (int i = 0; i < usernameCount; i++) {
            usernames[i] = scanner.nextLine();
        }

        for (String username : usernames) {
            if (isSpamBot(username)) {
                System.out.println(username);
            }
        }
    }
}