import java.util.Scanner;

public class solution {
    public static String getGreeting(String name) {
        return "Hello " + name + "!";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        System.out.println(getGreeting(name));
    }
}
