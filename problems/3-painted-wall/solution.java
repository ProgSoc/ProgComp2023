import java.util.Scanner;

public class solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String text = scanner.nextLine();
        System.out.println(brokenSequence(text));
    }

    public static int brokenSequence(String wall) {
        int count = 0;

        for (int i = 0; i < wall.length() - 1; i++) {
            String pair = wall.substring(i, i + 2);

            if (pair.equals("RG") || pair.equals("GB") || pair.equals("BR")) {
                continue;
            } else {
                count++;
            }
        }

        return count;
    }
}