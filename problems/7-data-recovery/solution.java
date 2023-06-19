import java.util.*;

public class solution {
    public static String recoverData(List<String> lines) {
        StringBuilder result = new StringBuilder();

        int lineLength = lines.get(0).length();
        for (int c = 0; c < lineLength; c++) {
            Map<Character, Integer> counts = new HashMap<>();
            for (String line : lines) {
                char ch = line.charAt(c);
                if (ch != ' ') {
                    counts.put(ch, counts.getOrDefault(ch, 0) + 1);
                }
            }

            if (counts.isEmpty()) {
                result.append(' ');
            } else {
                char ch = Collections.max(counts.entrySet(), Map.Entry.comparingByValue()).getKey();
                result.append(ch);
            }
        }

        return result.toString();
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