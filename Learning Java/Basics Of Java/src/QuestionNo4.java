public class QuestionNo4 {
    public static void main(String[] args) {
        System.out.println("Enter the number you want to get factorial of: ");
        int num = new java.util.Scanner(System.in).nextInt();
        long answer = factorial(num);
        System.out.println("The factorial of "+num+" is "+answer);

    }

    static int factorial(int n){
        if(n == 1)
            return 1;

        return n * factorial(n-1);

    }
}
