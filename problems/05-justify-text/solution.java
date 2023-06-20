import java.util.Scanner;
import java.util.ArrayList;

public class solution {
    public static String addWord(String line, String word) {
        if (line.length() == 0) {
            return word;
        }
        return line + ' ' + word;
    }

    public static String textJustification(int max_len, String text) {
        String[] words = text.split(" ");
        ArrayList<String> lines = new ArrayList<>();
        String currentLine = "";
        for (String word : words) {
            if (word.length() <= max_len) {
                String added = addWord(currentLine, word);
                if (added.length() <= max_len) {
                    currentLine = added;
                } else {
                    lines.add(currentLine);
                    currentLine = word;
                }
            } else {
                while (word.length() > max_len) {
                    if (!currentLine.isEmpty()) {
                        lines.add(currentLine);
                        currentLine = "";
                    }
                    lines.add(word.substring(0, max_len - 1) + '-');
                    word = word.substring(max_len - 1);
                }
                currentLine = word;
            }
        }
        lines.add(currentLine.stripLeading()); // appending the last line
        return String.join("\n", lines);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int max_length = scanner.nextInt();
        scanner.nextLine();
        String line = scanner.nextLine();
        System.out.println(textJustification(max_length, line));
        scanner.close();
    }
}