import java.util.*;

public class solution {
    public static String recoverData(List<String> lines) {
        // Your solution goes here
        return "";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lineCount = scanner.nextInt();
        scanner.nextLine();
        List<String> lines = new ArrayList<>();
        for (int i = 0; i < lineCount; i++) {
            String text = scanner.nextLine();
            lines.add(text.substring(1, text.length() - 1));
        }
        String recovered = recoverData(lines);
        System.out.println(recovered);
    }
}