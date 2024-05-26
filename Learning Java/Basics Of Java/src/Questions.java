import java.util.Scanner;

public class Questions {
    public static void main(String[] args) {

//        Program No.1
//          int j = 0;
//
//          for(j=0;j<11;j++){
//              System.out.println("J: "+ j);
//          }

//        Program No.2
//
//        System.out.println("This Program returns the sum of 1 to 10 natural numbers!");
//
//        int i = 0;
//        for (i=0;i<11; i++){
//            System.out.println(i+(i+1));
//        }
//        Program No.3
        System.out.println("Enter the num you want to get table of:  ");
        int num = new java.util.Scanner(System.in).nextInt();
        int x = 0;
        for(x=0;x<11;x++){
            int sum = num * x;
            System.out.println(num +" X "+ x + " = " + sum);
        }

//        Program No.4 (Hard One) TODO: Write a program that returns the factorial of the given number











    }
}
