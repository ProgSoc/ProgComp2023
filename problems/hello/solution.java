import java.util.Scanner;

public class solution {
    public static String getGreeting(String name) {
        String capitalizedName = name.substring(0, 1).toUpperCase() + name.substring(1).toLowerCase();
        return "Hello " + capitalizedName + "!";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        System.out.println(getGreeting(name));
    }
}
