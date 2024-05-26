import java.util.Scanner;

public class Exercise1 {
    public static void main(String[] args) {
        System.out.println("Note: Enter marks out of 20");

        System.out.println("Enter your marks in English: ");
        int english = new Scanner(System.in).nextInt();
        System.out.println("Enter your marks in Hindi: ");
        int hindi = new Scanner(System.in).nextInt();
        System.out.println("Enter your marks in Science: ");
        int science = new Scanner(System.in).nextInt();
        System.out.println("Enter your marks in Maths: ");
        int maths = new Scanner(System.in).nextInt();
        System.out.println("Enter your marks in Civics: ");
        int civics = new Scanner(System.in).nextInt();

        int sum = (english + maths + hindi + science + civics);
        int percentage =  (sum/100)*100;

        System.out.println("You Got '"+ sum +"'%");

    }
}
